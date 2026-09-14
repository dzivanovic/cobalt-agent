---
title: "ADR-002 Cobalt-Ion Distributed Protocol"
status: Active 
priority: P0
module: [Architecture]
phase: 1
complexity: M
tags: [cobalt, architecture, documentation, adr]
created: 2026-02-23
---

# ADR-002: Cobalt-Ion Distributed Protocol

## Status: ACCEPTED

## Decision

We implement a **Distributed Actor Model** using high-speed message brokers:

### Components

#### Cobalt (Mac - Python)
- **Role**: Chief of Staff, Router, Decision Maker
- **Technologies**: Python, FastAPI, Redis Pub/Sub, ZeroMQ
- **Responsibilities**:
  - LLM integration
  - Department routing
  - Tool orchestration
  - Memory management
  - Strategy execution

#### Ion (Windows - Rust)
- **Role**: Visualization, UI, Real-time Updates
- **Technologies**: Rust, Redis Pub/Sub, ZeroMQ
- **Responsibilities**:
  - Chart rendering
  - Order entry UI
  - Real-time price updates
  - Alert notifications
  - Human interaction

### Communication Protocol

**Format**: JSON payloads over message brokers

**Channels**:
```
cobalt→ion:routing       Cortex → Ion: Route user input
cobalt→ion:execute       Cortex → Ion: Execute tool
ion→cobalt:notification  Ion → Cortex: User action
ion→cobalt:heartbeat     Ion → Cortex: Health check
```

## Architecture

```
                    ┌───────────────┐
                    │    Mac        │
                    │   Cobalt      │
                    │   (Python)    │
                    └───┬───┬───────┘
                        │   │
              ┌─────────▼───▼───────┐
              │   Message Broker    │
              │   (Redis/ZeroMQ)    │
              └───┬───┬──────┬──────┘
                  │   │      │
    ┌──────────┐  │   └─┐    │
┌───▼────┐  ┌───▼────┐  │ ┌──▼─────┐
│ Ion    │  │ Ion    │  │ │  Ion   │
│ (Rust) │  │ (Rust) │  │ │ (Rust) │
│ Windows│  │ Windows│  │ │ Windows│
└────────┘  └────────┘  │ └────────┘
                        │
                  ┌─────▼──────┐
                  │   Redis    │
                  │  Pub/Sub   │
                  └────────────┘
```

## Implementation Details

### Cobalt (Python) - Publisher/Subscriber
```python
import redis
import json

class CobaltBroker:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)
        self.channel = 'cobalt/ion'
    
    def publish_routing(self, data: dict) -> None:
        self.redis.publish(self.channel, json.dumps({
            'type': 'routing',
            'payload': data
        }))
    
    def subscribe_notifications(self, callback):
        pubsub = self.redis.pubsub()
        pubsub.subscribe('ion/cobalt')
        for message in pubsub.listen():
            callback(message)
```

### Ion (Rust) - Subscriber/Publisher
```rust
use redis::{Connection, Commands};

struct IonBroker {
    conn: Connection,
    channel: String,
}

impl IonBroker {
    fn new() -> Self {
        let conn = redis::Connection::connect("redis://localhost:6379").unwrap();
        IonBroker {
            conn,
            channel: "ion/cobalt".to_string(),
        }
    }
    
    fn subscribe(&mut self) {
        self.conn.subscribe(&"cobalt/ion").unwrap();
    }
    
    fn publish(&mut self, data: &str) {
        self.conn.publish("ion/cobalt", data).unwrap();
    }
}
```

## Trade-offs

| Option | Pros | Cons |
|--------|------|------|
| REST API | Simple, HTTP compatible | High latency, synchronous |
| Message Brokers (Chosen) | Low latency, async, scalable | More complex setup |

## Next Steps

1. Implement Redis Pub/Sub in Python Cortex
2. Implement ZeroMQ bindings in Rust Ion
3. Create message schemas
4. Add reconnection logic

## References

- [Redis Pub/Sub Documentation](https://redis.io/docs/manual/pubsub/)
- [ZeroMQ Documentation](https://zeromq.org/documentation/)