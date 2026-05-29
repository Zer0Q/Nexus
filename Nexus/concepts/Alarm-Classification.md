# Alarm Classification

## Definition
Grouping alarms with a common set of alarm management requirements (testing, training, monitoring, audit). An alarm may belong to multiple classes. Classification is a management tool — it is distinct from prioritization, which serves the operator.

## Why It Matters
Not all alarms have the same lifecycle requirements. Classification allows organizations to apply appropriate management rigor: safety-critical alarms get extra scrutiny, while general process alarms follow standard procedures. Right-sizing the effort is key.

## Key Ideas
- **Defined in alarm philosophy:** required by ISA-18.2, but specific definitions left to the owner
- **Common classes:** safety critical, personnel protection, environmental, product quality, commercial loss, licensor requirements, company policy
- **Not source-based:** class assignment depends on requirements, not alarm source — all functional safety alarms can have different requirements
- **Cross-reference tool:** when alarm management software is used, classification helps manage and record compliance
- **Prevents accidental deletion:** classified alarms are protected from inadvertent changes
- **Right-size approach:** split out key "special" HMAs, leave rest as general class — don't classify every alarm
- **H2S example:** managed as a class with defined action/danger levels, special HMI handling, testing frequency, training, metrics, audit requirements

## Tradeoffs
- May seem to add paperwork and complexity — experience shows it is effective
- Over-classification creates management overhead without proportional benefit

## Related
- [[Highly-Managed-Alarm]]
- [[Alarm-Philosophy]]
- [[Alarm-Management-Lifecycle]]
- [[Alarm-Monitoring-and-Assessment]]

## Source
[[Fitzpatrick-Alarm-Lifecycle-and-Classes]]
