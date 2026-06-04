# Bad Data as Diagnostic

## Definition
Every data anomaly — missing values, "Other" selections, workaround spreadsheets, blank mandatory fields — is a process confessing exactly where it breaks. Bad data is free diagnostic information, not just noise to be cleaned.

## Why It Matters
Companies pay consultants serious money to locate process failure points. Their own data is volunteering them for free. Deleting bad records makes the model look better tomorrow, but the system that produced them keeps running, still generating the same problem.

## Key Ideas
- **EDA surfaces symptoms, not causes:** Exploratory Data Analysis finds missing values and outliers, but stopping at cleaning treats the symptom and discards the signal
- **Every anomaly tells a story:** blank field = system let transaction continue without it; outdated phone number = nobody owns that information; wrong cost center = users pick generic "Other" when right option doesn't exist
- **Go upstream:** "Why is the process generating this data in the first place?" — was the field optional when it shouldn't have been? Was the correct option available? Was master data maintained? Was the user forced to trade accuracy for speed?
- **Root cause questions:** did the system allow the omission? Was the correct cost center available? Had "Other" become everyone's shortcut? Was master data maintained?
- **Design processes that don't create the problem:** once you understand the real cause, design a process that stops creating bad data rather than cleaning it downstream

## Tradeoffs
- Requires investigative mindset instead of quick-fix data cleaning
- Frontline engagement needed to understand the "why" behind anomalies

## Related
- [[concepts/Visual-Management]]
- [[concepts/Poka-Yoke]]
- [[concepts/Gemba]]
- [[concepts/People-Process-Technology-Sequence]]

## Source
[[summaries/Gellida-Broken-Process-Broken-AI]]
