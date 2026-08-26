const I18N = {
  en: {
    tab_drc:'Daily Report Card', tab_pb:'PlayBook', reset:'Reset',
    header:'Header', day_grade:'Day grade', grade_ph:'A / B / C…',
    goal:'Goal (single focus of the day)', goal_ph:"That day's sole conscious focus",
    reminders:'Reminders / aphorisms to myself (one per line)', reminders_ph:'One per line',
    wrap_up:'Wrap-up', learned:'What I learned / improved upon today',
    changes:'Changes I need to make from today', overview:'Overview', easiest:'Easiest $50k',
    writeup:'Writeup', chart_drop:'Chart (drop a .png)', dz:'Drop your screenshot here (or click / paste)',
    build_pdf:'Generate PDF', build_pptx:'Generate SMB PlayBook PPTX',
    trade_name:'Trade name', bp_chart:'Overall market chart (optional divider slide)',
    fund_ph:'Why this ticker is on the radar (news, volume, gap, catalyst…)',
    main_chart:'Main chart', extra_chart:'Extra chart (optional)', lines_ph:'One key point per line',
    optional:'(optional — slide hidden if empty)', key_points:'Key points', detailed_review:'Detailed review',
    generating:'Generating…', done:'Generated ✓', dl_pdf:'Download PDF', preview:'Preview',
    dl_pptx:'Download PPTX', err:'Error: ', img_only:'Image files only (.png, .jpg)',
    pasted:'Screenshot pasted ✓', reset_confirm:'Clear all fields and images?', reset_done:'All cleared ✓',
  },
  fr: {
    tab_drc:'Daily Report Card', tab_pb:'PlayBook', reset:'Réinitialiser',
    header:'En-tête', day_grade:'Grade du jour', grade_ph:'A / B / C…',
    goal:'Goal (focus unique du jour)', goal_ph:'Le seul focus conscient du jour',
    reminders:'Rappels / aphorismes (un par ligne)', reminders_ph:'Un par ligne',
    wrap_up:'Bilan', learned:"Ce que j'ai appris / amélioré aujourd'hui",
    changes:'Changements à faire dès demain', overview:"Vue d'ensemble", easiest:'Easiest $50k',
    writeup:'Writeup', chart_drop:'Chart (glisser un .png)', dz:'Glisse ton screenshot ici (ou clic / coller)',
    build_pdf:'Générer le PDF', build_pptx:'Générer le PlayBook SMB (PPTX)',
    trade_name:'Nom du trade', bp_chart:'Chart marché global (slide divider optionnelle)',
    fund_ph:'Pourquoi ce ticker est sur le radar (news, volume, gap, catalyseur…)',
    main_chart:'Chart principal', extra_chart:'Chart extra (optionnel)', lines_ph:'Un point clé par ligne',
    optional:'(optionnel — slide masquée si vide)', key_points:'Points clés', detailed_review:'Review détaillée',
    generating:'Génération…', done:'Généré ✓', dl_pdf:'Télécharger le PDF', preview:'Aperçu',
    dl_pptx:'Télécharger le PPTX', err:'Erreur : ', img_only:'Fichier image uniquement (.png, .jpg)',
    pasted:'Screenshot collé ✓', reset_confirm:'Effacer tous les champs et images ?', reset_done:'Tout effacé ✓',
  },
};

let LANG = 'en';
try { LANG = localStorage.getItem('bse_lang') || 'en'; } catch (_) {}
const t = key => (I18N[LANG] && I18N[LANG][key]) || I18N.en[key] || key;

function applyLang() {
  document.documentElement.lang = LANG;
  document.querySelectorAll('[data-i18n]').forEach(el => { el.textContent = t(el.dataset.i18n); });
  document.querySelectorAll('[data-ph]').forEach(el => { el.placeholder = t(el.dataset.ph); });
  document.getElementById('tab-drc').textContent = t('tab_drc');
  document.getElementById('tab-pb').textContent = t('tab_pb');
  document.getElementById('reset-btn').textContent = t('reset');
  document.getElementById('lang-btn').textContent = LANG === 'en' ? 'FR' : 'EN';
  document.getElementById('drc-build').textContent = t('build_pdf');
  document.getElementById('pb-build').textContent = t('build_pptx');
}
function toggleLang() {
  LANG = LANG === 'en' ? 'fr' : 'en';
  try { localStorage.setItem('bse_lang', LANG); } catch (_) {}
  applyLang();
}
function nav(id, button) {
  document.querySelectorAll('.screen').forEach(screen => screen.classList.remove('on'));
  document.querySelectorAll('.ntab').forEach(tab => tab.classList.remove('on'));
  document.getElementById(`screen-${id}`).classList.add('on');
  button.classList.add('on');
}
function toggleTheme() {
  const light = document.documentElement.classList.toggle('light');
  document.getElementById('theme-btn').textContent = light ? '☀️' : '🌙';
  try { localStorage.setItem('bse_theme', light ? 'light' : 'dark'); } catch (_) {}
}
try {
  if (localStorage.getItem('bse_theme') === 'light') {
    document.documentElement.classList.add('light');
    document.getElementById('theme-btn').textContent = '☀️';
  }
} catch (_) {}

function flash(message, type='ok') {
  const alert = document.getElementById('alert');
  alert.textContent = message;
  alert.className = `alert on ${type}`;
  setTimeout(() => alert.classList.remove('on'), 3500);
}

const images = {};
const dropClears = [];
document.querySelectorAll('.drop').forEach(zone => {
  const key = zone.dataset.key;
  const setImage = dataUrl => {
    images[key] = dataUrl;
    zone.classList.add('filled');
    zone.querySelector('.dz').style.display = 'none';
    let image = zone.querySelector('img');
    if (!image) {
      image = document.createElement('img');
      zone.insertBefore(image, zone.firstChild);
    }
    image.src = dataUrl;
  };
  const clearImage = event => {
    if (event) event.stopPropagation();
    delete images[key];
    zone.classList.remove('filled');
    zone.querySelector('img')?.remove();
    zone.querySelector('.dz').style.display = '';
  };
  const handleFile = file => {
    if (!file || !file.type.startsWith('image/')) { flash(t('img_only'), 'err'); return; }
    const reader = new FileReader();
    reader.onload = () => setImage(reader.result);
    reader.readAsDataURL(file);
  };
  
  zone.querySelector('.clear').addEventListener('click', clearImage);
  dropClears.push(clearImage);
  
  ['dragenter','dragover'].forEach(name => zone.addEventListener(name, event => {
    event.preventDefault(); zone.classList.add('over');
  }));
  ['dragleave','drop'].forEach(name => zone.addEventListener(name, event => {
    event.preventDefault(); zone.classList.remove('over');
  }));
  zone.addEventListener('drop', event => handleFile(event.dataTransfer.files[0]));
  
  // --- CORRECTION DÉFINITIVE PROBLÈME 1 (COMPATIBILITÉ 100% SAFARI / IOS) ---
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = 'image/*';
  input.style.position = 'absolute';
  input.style.left = '-9999px';
  input.style.opacity = '0';
  zone.appendChild(input);

  input.addEventListener('change', () => {
    if (input.files[0]) {
      handleFile(input.files[0]);
      input.value = ''; 
    }
  });

  zone.addEventListener('click', (event) => {
    if (event.target !== zone.querySelector('.clear')) {
      input.click();
    }
  });
  // -------------------------------------------------------------------------

  zone.addEventListener('mouseenter', () => { window.__pasteTarget = key; window.__pasteSet = setImage; });
  zone.addEventListener('mouseleave', () => {
    if (window.__pasteTarget === key) { window.__pasteTarget = null; window.__pasteSet = null; }
  });
});

document.addEventListener('paste', event => {
  const active = document.activeElement;
  if (active && active.matches('input, textarea, [contenteditable="true"]')) return;
  if (!window.__pasteTarget || !window.__pasteSet || !event.clipboardData) return;
  const item = Array.from(event.clipboardData.items).find(entry => entry.type.startsWith('image/'));
  if (!item) return;
  event.preventDefault();
  const file = item.getAsFile();
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => window.__pasteSet(reader.result);
  reader.readAsDataURL(file);
  flash(t('pasted'));
});

const SEGS = ['Temp', '9:30-11', '11-12', '12-2', '2-4'];
document.getElementById('drc-segments').innerHTML =
  '<div class="g6"><div class="seg-name"></div><label>Grade</label><label>PTD Only</label><label>Sizing</label><label>In My Favor</label><label>Comments</label></div>' +
  SEGS.map((segment, index) => `<div class="g6" style="margin-bottom:6px">
    <div class="seg-name">${segment}</div><input id="seg${index}-grade"><input id="seg${index}-ptd">
    <input id="seg${index}-sizing"><input id="seg${index}-favor"><input id="seg${index}-comments">
  </div>`).join('');

const STAT_HINTS = ['RVOL','Avg Volume','Float','Institutional Ownership','ATR','Short Interest',"Day's Range",'Insider Ownership','$VIX','Gap %'];
document.getElementById('pb-stats').innerHTML = STAT_HINTS.map((hint, index) => `
  <div class="stat-row">
    <input id="pb-stat-name${index}" value="${hint}" placeholder="${hint}">
    <input id="pb-stat-value${index}" placeholder="Value">
  </div>`).join('');

const GRADE_CATS = ['Big Picture','Intraday Fundamentals','Stock Selection','Technical Analysis',
  'Trade Strategy','Risk Management','Reading the Tape','Technology','Review: What Can You Do Better?'];
document.getElementById('pb-grades').innerHTML = GRADE_CATS.map((category, index) => `
  <div><label>${category}</label><input id="grade${index}" type="number" min="1" max="10" placeholder="1–10"></div>`).join('');

const value = id => (document.getElementById(id)?.value || '').trim();

function updateLineCounts() {
  document.querySelectorAll('.line-limited').forEach(field => {
    const max = Number(field.dataset.maxLines || 0);
    const count = field.value.split('\n').filter(line => line.trim()).length;
    const display = document.querySelector(`.line-count[data-for="${field.id}"]`);
    if (display) {
      display.textContent = `${count} / ${max}`;
      display.classList.toggle('over', count > max);
    }
  });
}
document.querySelectorAll('.line-limited').forEach(field => field.addEventListener('input', updateLineCounts));

const DRAFT_KEY = 'bse_template_first_draft_v22';
function saveDraft() {
  const draft = {};
  document.querySelectorAll('input, textarea, select').forEach(field => {
    if (field.id && field.type !== 'file') draft[field.id] = field.value;
  });
  try { localStorage.setItem(DRAFT_KEY, JSON.stringify(draft)); } catch (_) {}
}
function restoreDraft() {
  try {
    const draft = JSON.parse(localStorage.getItem(DRAFT_KEY) || '{}');
    Object.entries(draft).forEach(([id, stored]) => {
      const field = document.getElementById(id);
      if (field) field.value = stored;
    });
  } catch (_) {}
}
let saveTimer;
document.addEventListener('input', () => {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(saveDraft, 250);
});

function resetAll() {
  if (!confirm(t('reset_confirm'))) return;
  document.querySelectorAll('input:not([type=button]), textarea').forEach(field => { field.value = ''; });
  dropClears.forEach(clear => clear());
  document.querySelectorAll('.dl').forEach(box => { box.classList.remove('on'); box.innerHTML = ''; });
  try { localStorage.removeItem(DRAFT_KEY); } catch (_) {}
  setTodayDefaults(); updateLineCounts(); flash(t('reset_done'));
}

function localDateISO() {
  const now = new Date();
  const offset = now.getTimezoneOffset();
  return new Date(now.getTime() - offset * 60000).toISOString().slice(0, 10);
}
function setTodayDefaults() {
  ['drc-date','pb-date'].forEach(id => {
    const field = document.getElementById(id);
    if (field && !field.value) field.value = localDateISO();
  });
}

function overLineLimit() {
  return Array.from(document.querySelectorAll('.line-limited')).some(field => {
    const max = Number(field.dataset.maxLines || 0);
    return field.value.split('\n').filter(line => line.trim()).length > max;
  });
}

document.getElementById('drc-build').addEventListener('click', async () => {
  const button = document.getElementById('drc-build');
  button.disabled = true; button.textContent = t('generating');
  const data = {
    date:value('drc-date'), grade:value('drc-grade'), goal:value('drc-goal'), reminders:value('drc-reminders'),
    learned:value('drc-learned'), changes:value('drc-changes'), overview:value('drc-overview'), easiest:value('drc-easiest'),
    segments:SEGS.map((_, index) => ({grade:value(`seg${index}-grade`),ptd:value(`seg${index}-ptd`),sizing:value(`seg${index}-sizing`),favor:value(`seg${index}-favor`),comments:value(`seg${index}-comments`)})),
    tickers:[1,2].map(number => ({ticker:value(`t${number}-ticker`),pnl:value(`t${number}-pnl`),writeup:value(`t${number}-writeup`),chart:images[`t${number}-chart`] || null})),
  };
  try {
    const response = await fetch('/build-drc',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
    const json = await response.json(); if (!response.ok) throw new Error(json.error || '?');
    const dl = document.getElementById('drc-dl');
    dl.innerHTML = `<a href="/download/${json.session_id}/pdf">${t('dl_pdf')}</a> · <a href="/view/${json.session_id}.pdf" target="_blank">${t('preview')}</a>`;
    dl.classList.add('on'); flash(t('done'));
  } catch (error) { flash(t('err') + error.message,'err'); }
  finally { button.disabled = false; button.textContent = t('build_pdf'); }
});

document.getElementById('pb-build').addEventListener('click', async () => {
  if (overLineLimit()) { flash('Too many bullet lines in one or more template sections.', 'err'); return; }
  const button = document.getElementById('pb-build');
  button.disabled = true; button.textContent = t('generating');
  const grades = {};
  GRADE_CATS.forEach((category,index) => { const grade = value(`grade${index}`); if (grade) grades[category] = grade; });
  const statRows = STAT_HINTS
    .map((_,index) => ({name:value(`pb-stat-name${index}`),value:value(`pb-stat-value${index}`)}));
  // Section counts as filled only when a value is set or a label was customized;
  // otherwise the untouched default labels alone would force the slide visible.
  const statsFilled = statRows.some(stat => stat.value || (stat.name && !STAT_HINTS.includes(stat.name)));
  const fundamentalsStats = statsFilled ? statRows : [];
  const data = {
    trade_name:value('pb-name'), trader:value('pb-trader'), ticker:value('pb-ticker'), date:value('pb-date'),
    bp_chart:images['bp-chart'] || null, spy_note:value('pb-spy-note'), qqq_note:value('pb-qqq-note'),
    spy_chart:images['spy-chart'] || null, qqq_chart:images['qqq-chart'] || null,
    fundamentals:value('pb-fund'), fundamentals_stats:fundamentalsStats,
    ta_chart:images['ta-chart'] || null, ta_chart2:images['ta-chart2'] || null,
    strategy:value('pb-strategy'), tm_chart:images['tm-chart'] || null,
    risk_amount:value('pb-risk-amount'), daily_stop_pct:value('pb-daily-stop-pct'),
    risk_details:value('pb-risk-details'), stop_details:value('pb-stop-details'),
    tape:value('pb-tape'), tape_chart:images['tape-chart'] || null, tape_url:value('pb-tape-url'),
    
    // --- CORRECTION PROBLÈME 2 : Double mapping pour le backend ---
    technology:value('pb-tech'), 
    technology_chart:images['technology-chart'] || null, 
    tech_chart:images['technology-chart'] || null,
    // --------------------------------------------------------------
    
    review_points:value('pb-review-pts'), review_detail:value('pb-review-detail'), grades,
  };
  try {
    const response = await fetch('/build-playbook',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
    const json = await response.json(); if (!response.ok) throw new Error(json.error || '?');
    const dl = document.getElementById('pb-dl');
    dl.innerHTML = `<a href="/download/${json.session_id}/pptx">${t('dl_pptx')}</a>`;
    dl.classList.add('on'); flash(t('done'));
  } catch (error) { flash(t('err') + error.message,'err'); }
  finally { button.disabled = false; button.textContent = t('build_pptx'); }
});

restoreDraft(); setTodayDefaults(); updateLineCounts(); applyLang();