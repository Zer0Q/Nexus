# Cloud GPU Cost Recovery

## Definition
ROI calculation for replacing cloud GPU rental with local hardware like the DGX Spark. At $1,900/month cloud GPU spend, a $2,999 DGX Spark pays for itself in ~1.6 months, redirecting ~$22,000 back into the business in the first year instead of someone else's data center.

## Why It Matters
For AI freelancers and builders who rent compute by the hour, the cloud GPU bill is essentially profit walking out the door. Owning the hardware turns a variable cost into a one-time investment with minimal ongoing expenses.

## Key Ideas
- **Cloud burn**: A100 80GB ($600-1,200/mo), H100 ($1,000-2,500/mo), hosted 70B inference ($300-900/mo)
- **Total freelancer cloud spend**: $1,500-3,000/month
- **DGX Spark monthly**: ~$8-15 electricity at ~200W work hours
- **Payback period**: ~1.6 months at $1,900/month cloud habit
- **First-year recovery**: ~$22,000 redirected from cloud to your business
- After payback, the ~$1,890/month you used to hand a rental company is margin you keep

## Tradeoffs
- Upfront $2,999 is a real check
- Only makes sense if you're already bleeding $1,000+/month on cloud GPUs
- If you just chat with a 7B occasionally, a cheap edge device is smarter
- Hardware can become obsolete; cloud always has the latest

## Related
- [[DGX-Spark]] -- the hardware enabling this cost recovery
- [[DGX-Spark-Specs]] -- what you're buying
- [[Local-AI-Mindset-Shift]] -- the behavioral change after going local
- [[Hardware-Reality-of-Local-AI]] -- broader hardware economics

## Source
[[w1nklerr-DGX-Spark-Cost-Recovery]]
