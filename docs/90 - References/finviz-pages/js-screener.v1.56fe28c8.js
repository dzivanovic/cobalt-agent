function simpleFetch(url, options) {
  return fetch(url, options)
    .then(function (response) {
      if (!response.ok) return
      return response
    })
    .catch(function () {})
}

function getCurrentDateInMs() {
  return new Date().valueOf()
}

function getIsDocumentVisible() {
  return document.visibilityState === 'visible' || document.hidden === false
}

/**
 * Calls the callback at most every `interval` milliseconds if the window is visible.
 *
 * @param {number} interval in ms
 * @param {() => void} callback
 */
function intervalCallbackOnWindowVisible(interval, callback) {
  var nextRefresh = getCurrentDateInMs() + interval
  /** @type {NodeJS.Timeout} */
  var refreshTimeout = null

  function refresh() {
    nextRefresh = getCurrentDateInMs() + interval
    // Queue next refresh
    refreshTimeout = setTimeout(refresh, interval)
    // Call callback asynchronously
    setTimeout(callback, 0)
  }

  document.addEventListener('visibilitychange', function () {
    clearTimeout(refreshTimeout)

    if (getIsDocumentVisible()) {
      var currentDateMs = getCurrentDateInMs()
      // Refresh if the document is stale, otherwise set a timeout to refresh later
      if (nextRefresh <= currentDateMs) {
        refresh()
      } else {
        refreshTimeout = setTimeout(refresh, nextRefresh - currentDateMs)
      }
    }
  })

  if (getIsDocumentVisible()) {
    refreshTimeout = setTimeout(refresh, interval)
  }
}

function ScreenerPresetsChange(value, url) {
  if (value === '__save_screen') {
    window.location = 'screener_presets?' + url
  } else if (value === '__edit_screens') {
    window.location = 'screener_presets'
  } else if (value !== '') {
    window.location = 'screener?' + value
  }
  document.getElementById('screenerPresetsSelect').selectedIndex = 0
}

function ScreenerChartTypeChange(select, event) {
  const prevOption = Array.from(select.options).find((option) => option.hasAttribute('selected'))

  if (select.value === '/elite') {
    event.preventDefault()

    if (prevOption) prevOption.selected = true
    window.openEliteFeaturesDialog?.('advanced-chart')
  } else {
    window.location.href = select.value
  }
}

async function SavePortfolio(count, url) {
  if (count > window.portfolioRowsLimit) {
    if (
      !(await window.openGenericConfirmDialog(
        "There's " +
          window.portfolioRowsLimit +
          ' tickers limit per portfolio, only first ' +
          window.portfolioRowsLimit +
          ' will be saved. Save anyway?'
      ))
    ) {
      return
    }
  }
  window.location = 'screener_portfolio_add?' + url
}

async function OpenInCompare(count, url) {
  if (count > window.compareTickersLimit) {
    if (
      !(await window.openGenericConfirmDialog(
        'Compare supports up to ' +
          window.compareTickersLimit +
          ' tickers, only the first ' +
          window.compareTickersLimit +
          ' will be opened. Open anyway?'
      ))
    ) {
      return
    }
  }
  window.location = 'screener_compare_open?' + url
}

function OnExport() {
  window.gtag && window.gtag('event', 'screener_export_click', window.screenerExportClickGtmPayload)
  return true
}

var refreshId = 'screener-content'
var refreshTotalId = 'screener-total'
var refreshComboId = 'screener-page-select'
var refreshPaginationId = 'screener_pagination'
var refreshTableId = 'screener-table'

var refreshEmptyTableId = 'js-screener-body-empty'

function ScreenerRefreshInit(refresh, initVersion) {
  if (refresh > 0) {
    intervalCallbackOnWindowVisible(refresh * 1000, Refresh)
  }

  if (initVersion !== undefined) currentVersion = initVersion.toString()
}

function getInnerHTML(pageDocument, elementId) {
  let element = pageDocument.getElementById(elementId)
  if (element) {
    return element.innerHTML
  }
  return null
}

function setInnerHTML(pageDocument, elementId, innerHTMLContent) {
  let element = pageDocument.getElementById(elementId)
  if (element) {
    element.innerHTML = innerHTMLContent
  }
}

var RefreshPreviousVersion = null
var RefreshPreviousTickerData = {}
var RefreshCounter = 0
function OnRefresh(result) {
  const newDocument = new DOMParser().parseFromString(result, 'text/html')
  if (!newDocument) return

  const shouldReplaceWholeScreenerContent =
    !!newDocument.getElementById(refreshEmptyTableId) || !!document.getElementById(refreshEmptyTableId)

  const tableContainerElement = newDocument.getElementById(refreshId)
  // Bail out, there’s probably something wrong with the document (failed loading,…)
  if (!tableContainerElement) return

  const newTotalElementContent = getInnerHTML(newDocument, refreshTotalId)
  const newPageSelectElementContent = getInnerHTML(newDocument, refreshComboId)
  const newPaginationElementContent = getInnerHTML(newDocument, refreshPaginationId)
  const newTableElementContent = getInnerHTML(newDocument, refreshTableId)

  const changeSum =
    newTotalElementContent + newPageSelectElementContent + newPaginationElementContent + newTableElementContent

  var divUpdated = false
  if (RefreshPreviousVersion !== changeSum || RefreshCounter === 100) {
    RefreshCounter = 0

    if (shouldReplaceWholeScreenerContent) {
      window.ScreenerTimeframeReactUnmount()
      document.getElementById(refreshId).innerHTML = tableContainerElement.innerHTML
      window.ScreenerTimeframeReactMount()
    } else {
      setInnerHTML(document, refreshTotalId, newTotalElementContent)
      setInnerHTML(document, refreshComboId, newPageSelectElementContent)
      setInnerHTML(document, refreshPaginationId, newPaginationElementContent)
      setInnerHTML(document, refreshTableId, newTableElementContent)
    }

    window.dispatchEvent(new Event('html-refresh'))

    divUpdated = true

    setTimeout(function () {
      var imgs = document.getElementsByTagName('img')
      var rev = new Date().getTime()
      for (var i = 0; i < imgs.length; i++) {
        var img = imgs[i]
        var srcset = img.srcset
        if (srcset.indexOf('/chart?') <= 0) {
          continue
        }

        ScreenerUpdateImageRev(img, rev)
      }
    }, 16)
  } else {
    RefreshCounter++
    var tickerData = ScreenerGetCommentData(result)

    var imgs = document.getElementsByTagName('img')
    var rev = new Date().getTime()
    for (var i = 0; i < imgs.length; i++) {
      var img = imgs[i]
      var srcset = img.srcset
      if (srcset.indexOf('/chart?') <= 0) {
        continue
      }

      var ticker = ScreenerGetUrlParameterByName('t', srcset)
      if (tickerData[ticker] !== RefreshPreviousTickerData[ticker]) {
        ScreenerUpdateImageRev(img, rev)
      }
    }
  }

  RefreshPreviousVersion = changeSum
  RefreshPreviousTickerData = ScreenerGetCommentData(result)

  window.gtag && window.gtag('event', 'refresh', { event_category: 'page' })

  if (divUpdated && typeof window.refreshAds === 'function') {
    window.refreshAds('#' + refreshId + ' [id*=IC_D_]')
  }
}

var currentVersion = null

function Refresh() {
  var rev = (window.location.search.length === 0 ? '?' : '&') + 'rev=' + +new Date()
  simpleFetch(window.location.href + rev, {
    headers: {
      'X-Theme': window.FinvizSettings.hasDarkTheme
        ? 'dark'
        : window.FinvizSettings.hasRedesignEnabled
          ? 'light'
          : 'legacy',
    },
  })
    .then(function (res) {
      if (!res) {
        return Promise.resolve(undefined)
      }

      if (!checkVersionMatches(res.headers)) {
        window.location.reload()
        return
      }
      return res.text()
    })
    .then(function (data) {
      if (data === undefined) {
        return
      }
      OnRefresh(data)
    })
}

/*
 * Parses
 * ...
 * <!-- TS
 * A|1|2
 * B|3|4
 * TE -->
 * ...
 * to { "A": "1|2", "B": "3|4" }
 */
function ScreenerGetCommentData(html) {
  var commentStartStr = '<!-- TS\n'
  var commentStart = html.indexOf(commentStartStr)
  if (commentStart < 0) return
  commentStart += commentStartStr.length
  var commentEnd = html.indexOf('TE -->\n', commentStart)
  if (commentEnd < 0) return

  var comment = html.substring(commentStart, commentEnd)
  var rows = comment.split('\n')
  var tickerData = {}
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i]
    if (row === '') {
      continue
    }
    var columns = row.split('|')
    tickerData[columns[0]] = columns[1] + '|' + columns[2]
  }
  return tickerData
}

function ScreenerGetUrlParameterByName(name, url) {
  name = name.replace(/[\[\]]/g, '\\$&')
  var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
    results = regex.exec(url)
  if (!results) return null
  if (!results[2]) return ''
  return decodeURIComponent(results[2].replace(/\+/g, ' '))
}

function ScreenerUpdateImageRev(img, rev) {
  img.srcset = img.srcset
    .split(', ')
    .map(function (set) {
      var setParts = set.trim().split(' ').reverse()
      var url = setParts.pop()
      return [updateRevForProp(url, rev)].concat(setParts.reverse()).join(' ')
    })
    .join(', ')
}

function updateRevForProp(prop, rev) {
  var srcRevPos = prop.indexOf('&rev=')
  if (srcRevPos >= 0) return prop.substr(0, srcRevPos) + '&rev=' + rev

  return prop + '&rev=' + rev
}

function checkVersionMatches(headers) {
  var refreshVersion = headers.get('X-REFRESH-VERSION')
  if (currentVersion === null) currentVersion = refreshVersion

  return refreshVersion === null || refreshVersion === currentVersion
}

document.addEventListener('keyup', ({ key, shiftKey }) => {
  const target = `${shiftKey ? 'Shift' : ''}${key}`

  if (key === 'ArrowLeft' || key === 'ArrowRight') {
    if (!document.activeElement?.matches('html, body')) return

    const wrapper = '#screener_pagination'
    const firstArrow = 'a:first-child:is(.screener-pages.is-prev, .tab-link):not(.is-selected)'
    const lastArrow = 'a:last-child:is(.screener-pages.is-next, .tab-link):not(.is-selected)'
    const firstPage = `${firstArrow} + a.screener-pages`
    const lastPage = `a.screener-pages:has(+ ${lastArrow})`

    const selector = {
      ArrowLeft: `${wrapper} > ${firstArrow}`,
      ArrowRight: `${wrapper} > ${lastArrow}`,
      ShiftArrowLeft: `${wrapper} > ${firstPage}`,
      ShiftArrowRight: `${wrapper} > ${lastPage}`,
    }

    document.querySelector(selector[target])?.click()
  }
})
