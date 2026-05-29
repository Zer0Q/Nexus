---
title: "What Is High-Performance HMI?"
source: "https://www.realpars.com/blog/high-performance-hmi?utm_source=chatgpt.com"
author:
  - "[[GregoryDuranso]]"
published: 2001-08-05
created: 2026-05-29
description:
tags:
  - "clippings"
summary:
---
**High-Performance HMI** is the industry answer for a standardized, easy to use, and more productive HMI graphics system to implement and in some cases, replace a poorly designed HMI.

As we know, operator control of processes is done using a graphical representation of the process, known as an [HMI](https://realpars.com/hmi-panel/), or Human Machine Interface.

![](https://www.youtube.com/watch?v=5GEvFF8pGlc)

### A properly designed HMI

A properly designed HMI will support a smooth and stable operation of the process as well as notify the operator of an abnormal condition. However, this isn’t always the case.

Many HMIs were poorly designed and implemented, leading to situations that can compromise safety, quality, and profitability.

![Poorly Designed HMI](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae0_Poorly-Designed-HMI.png)

Poorly Designed HMI

Many current HMIs make use of

– a broad spectrum of colors,

– unnecessary graphics,

– visual distractions, and

– lack of overall situational awareness.

These, in turn, can result in negative consequences.

Some of these consequences can include poor operating procedures, such as running by the alarms, where an operator is only responding to alarms and not understanding the root cause of the alarm conditions.

In other cases, a poorly designed HMI will result in avoidable upsets and increase the likelihood of less than the optimum response to an abnormal situation.

In the worst cases, a poorly designed HMI has been identified as a contributing factor in some industrial accidents.

You can an example of a poorly designed HMI below.

![Colorful Poorly Designed HMI](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae3_Colorful-Poorly-Designed-HMI.png)

Colorful Poorly Designed HMI

### HMI design requirements

Let’s talk about how we got here. Early HMIs were simple depictions of the P&ID of the process that they were controlling and monitoring. This was mostly from the limitations of the computing and graphics power of the times.

As computing power and graphics processors advanced, so did the mindset that a highly complex, data-filled, and visually striking HMI should follow.

We see flickering flames to represent a flare, moving rail cars in loading bays, some have gone as far as to take digital photos of the actual process floor and overlay data on the HMI screens!

Add this mindset to the thousands of systems integrators, and we end up with an industry with no standard displays. Even identical processes can have vastly different HMI screens, depending on who implemented them and customer desires.

There are HMIs all around the world with

– inconsistent navigation,

– difficult to understand data being presented,

– improper alarm depictions, and

– a lack of display methodologies

presenting the state of the operating equipment.

![HMI Design Requirments](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae1_HMI-Design-Requirments.png)

HMI Design Requirments

### ISA-101 HMI design standard

Let’s move away from these HMIs and learn about the High-Performance HMI.

In 2003, the International Society of Automation, or ISA, tasked a group of end-users, operators, and engineers to start working on a standard.

In 2015, twelve years later, they published the ISA-101 HMI Design Standard. It is the set of guidelines, principles, and philosophies for developing graphics on a process HMI. This standard is meant to create

– a more functional,

– easy to understand, and

– information-driven

operator interface.

![ISA-101 HMI Design Standard](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae4_ISA-101-HMI-Design-Standard.png)

ISA-101 HMI Design Standard

#### Proper use of color

Here we are going to cover the basic concepts of High-Performance HMI. One concept is the proper use of color. Moving away from the intense and colorful graphics, the High-Performance HMI is developed in grayscale, with color intended to be the attention-getter.

Gone are the days of red and green to indicate running or not running. In a grayscale screen, the use of color is meant to indicate an abnormal situation very quickly. It has been shown that the new use of color alone has resulted in a 48% improvement in detecting abnormal situations before alarms occur.

A grayscale screen with no color present means a normal operating plant with no alarms. A quick glance by an operator can confirm this and productivity can increase as the operators do not have to spend time studying a screen to look for abnormal situations.

![Proper Use Of Color](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fadf_Proper-Use-Of-Color.png)

Proper Use Of Color

#### Use of information over data

Another concept is the use of information over data. Many HMIs will have dozens or more data points visible on the screen, but nothing for an operator to determine what that data means.

A pressure indicator could read 900 psi, but is that a good thing or a bad thing? By utilizing an indicator of normal range with a process variable, the operator can make a quick decision to take action to correct a situation that is trending away from normal.

![Use Of Information Over Data](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678faf8_Use-Of-Information-Over-Data.png)

Use Of Information Over Data

##### High-performance HMI trends

Speaking of trends, we now are seeing embedded or always visible trends on important process variables. By making these trends always visible, the operator can see a quick overview of historical data and evaluate for any necessary process adjustments before a product runs out of specification or a tank overflows, both time consuming and costly mistakes that can now be avoided.

![HMI Trends](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae2_HMI-Trends.png)

HMI Trends

#### Keeping the screen simple

A very important concept in High-Performance HMI is keeping the screen simple and uncluttered. A simple depiction of a vessel with a valve and pump is all that is necessary. Along with that are easy to find **navigation** buttons that will take the operator to the next step in the overall process.

![HMI navigation buttons](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fafe_HMI-navigation-buttons.png)

HMI navigation buttons

##### High-performance HMI colors

There is no need to show bulkhead fittings, flanges, or non-essential 3D pipe objects. Instead, an ISA valve and pump, using a line to depict process flow are the standard.

When depicting the status of a pump or valve, instead of red and green for running or not running on a pump or open and closed on a valve, High-Performance HMI will use a dark gray status for a pump that is stopped and white for a pump that is running. For a pump that does not send feedback to [SCADA](https://realpars.com/scada-applications/), it will be depicted as medium gray.

![HMI Design Standards](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678faea_HMI-Design-Standards.png)

HMI Design Standards

### High-performance HMI display hierarchy

Proper display hierarchy is critical to a High-Performance HMI. By creating a hierarchical system of displays, the operators can have overall situational awareness, and the ability to drill down to very specific data points when necessary.

There are four levels of hierarchy in the High-Performance HMI.

#### 1) Overall situational awareness

Level 1 is used for overall situational awareness. An operator can see the entire process at a very high level from this screen.

![Overall Situational Awareness](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae6_Overall-Situational-Awareness.png)

Overall Situational Awareness

#### 3) Equipment details

Level 3 is the equipment details screen, such as a pump or a valve. It will include even more detailed data on that particular process.

![Equipment Details](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae7_Equipment-Details.png)

Equipment Details

#### 4) Diagnostics

Finally, Level 4 is the diagnostics screen. This will give the operator access to very detailed information on a processing device and is accessed for troubleshooting purposes.

![Diagnostics Screen](https://cdn.prod.website-files.com/65f854814fd223fc3678ea53/65f854814fd223fc3678fae8_Diagnostics-Screen.png)

Diagnostics Screen

High-Performance HMI is still a moving target and is still subject to the preferences of the stakeholders. However, it has been shown that when presented with the concepts of High-Performance HMI, operators are eager and excited to implement it into their system.

While all systems are different, utilizing a more standardized model will vastly improve productivity, quality, and safety. Thank you for watching this video, and be sure to look for Part 2, High-Performance HMI Design Basics.

Some of the graphics and the HMI screens used in this video are from the [High-Performance HMI handbook](https://www.amazon.com/High-Performance-HMI-Handbook/dp/0977896919) which is a great reference if you want to dig deeper into this topic.

We recommend checking the following related articles, if you haven’t already, to have a better understanding of High-Performance HMI Philosophy:

[▶ What is High-Performance HMI? (Part 1 of 4)](https://realpars.com/high-performance-hmi/)

[High-Performance HMI Design Basics (Part 2 of 4)](https://realpars.com/hmi-design/)

[Development of High-Performance HMI Philosophy (Part 3 of 4)](https://realpars.com/HMI-Philosophy)

[Detailed Design Principles of High-Performance HMI Display (Part 4 of 4)](https://realpars.com/HMI-Display)

If you have any questions about High-Performance HMI and Design standards, add them in the comments below and we will get back to you in less than 24 hours.

Got a friend, client, or colleague who could use some of this information? Please share this article.

**The RealPars Team**

![Profile Icon](https://cdn.prod.website-files.com/65f854814fd223fc3678ea45/65f854814fd223fc3678ea84_icon-profile.svg) ![Calendar Icon](https://cdn.prod.website-files.com/65f854814fd223fc3678ea45/65f854814fd223fc3678ea86_icon-calendar.svg)

2020-12-07