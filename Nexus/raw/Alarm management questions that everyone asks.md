---
title: "Alarm management questions that everyone asks"
source: "https://www.isa.org/intech-home/2020/march-april/features/alarm-management-questions-that-everyone-asks?utm_source=chatgpt.com"
author:
  - "[[Donald G. Dunn and Nicholas P. Sands]]"
  - "[[PE]]"
  - "[[CAP]]"
published:
created: 2026-05-29
description: "ISA"
tags:
  - "clippings"
summary:
---
- By Donald G. Dunn, Nicholas P. Sands, PE, CAP
- March 31, 2020
- Continuous & Batch Processing

### Summary

**Fast Forward**

- The article is a comprehensive overview of alarm management questions everyone asks.
- Alarm systems should provide the right indication at the right time for operators to respond and avoid undesired consequences.
- ANSI/ISA-18.2 is the authoritative standard on alarm management, supported by seven technical reports with additional guidance.

### How to achieve an effective and efficient alarm management program

Understanding and implementing effective alarm management brings many operational benefits. This article highlights common questions and answers to help you understand alarm management.

#### What is alarm management?

Alarm management is the taming of the alarm system, changing it from a mixed alarm and awareness notification system with almost random priorities to a true operator support tool that notifies operators to take the right action at the right time to avoid an undesired consequence.

This transformation includes applying the definition of “alarm” in a process called rationalization to remove the notifications that are not truly alarms.

*Alarm (n): audible and/or visible means of indicating to the operator an equipment malfunction, process deviation, or abnormal condition requiring a timely response.*

Also, during rationalization, the consequences and corrective actions for each alarm are documented, so that the operators can be trained to respond. The alarm system is monitored and assessed against performance targets to understand what issues need to be fixed to keep the system working for the operator. There are many more steps in the life cycle of alarm management, but the key steps of removing things that are not really alarms, training the operators to respond, and monitoring system performance provide most of the benefits.

#### Which alarm management standard do I follow: ISA-18.2, IEC 62682, or EEMUA 191?

You can build a successful alarm management program with any of the three. The activities for the full alarm management life cycle (figure 1) are more clearly organized in the ISA and International Electrotechnical Commission (IEC) standards. As standards, these documents describe what should be included in an alarm management program, but not how to do those things. Engineering Equipment and Materials Users Association (EEMUA) 191, as a guideline and not a standard, addresses both what and how to a limited extent. The seven ISA-18.2 technical reports address the “how” in much greater detail, aligned to the ISA standard.

As far as the standards go, ANSI/ISA-18.2 and IEC 62682 are almost the same, as the IEC version was only slightly modified from the ISA version. ISA-18.2 was first published in 2009 and was designed not to conflict with the EEMUA 191 guideline and the NAMUR (the German Standardization Association for Measurement and Control in Chemical Industries) NA102 worksheet. The goal was to build a consistent set of terminology and activities for alarm management. Today, ISA-18.2 is the authoritative standard on alarm management.

Regulatory requirements can be a factor in choosing to follow the standards on alarm management.

---

![](https://www.isa.org/getmedia/daca735e-884f-462f-b990-30b4c6d50ed7/MA_2020_Cont-Batch-Process-fig1.gif?width=364&height=328&ext=.gif)

Figure 1. The alarm management life cycle.

---

#### Is an alarm management program a regulatory requirement?

Yes, alarm management can be a regulatory requirement, depending on the industry and the country. In the U.S., facilities covered by the Occupational Safety and Health Administration (OSHA) Process Safety Management (PSM) and the Environmental Protection Agency (EPA) Risk Management Plan (RMP) can meet requirements using the ISA or IEC standard as recognized and generally accepted good engineering practice (RAGAGEP). The pharmaceutical industry can meet Food and Drug Administration (FDA) Current Good Manufacturing Practice (CGMP) requirements using the standards. These OSHA, EPA, and FDA programs predate the alarm management standards, so there is not an explicit reference to alarm management, but there are references to alarms.

The pipeline industry, regulated by the Pipeline and Hazardous Materials Safety Administration (PHMSA), specifically requires alarm management since 2012 because of incidents. The pipeline industry often uses API RP1167, which is also derived in part from ISA-18.2.

In Europe, facilities covered by the Seveso directives also have a requirement for alarm management. The ISA or IEC standard would be good guidance. In the U.K., EEMUA 191 is still often used, as the Health and Safety Executive (HSE) has not updated its 2000 information sheet on Better Alarm Handling to reference BS62682, the British Standards version of IEC 62682, versus the EEMUA 191 guideline.

Aside from regulatory requirements, many companies now have policies on alarm management after incidents or have requirements for alarm management from their insurance companies. So, there are several ways to have alarm management as a requirement.

#### How much does implementing an alarm management program cost?

There are many ways to implement an alarm management program, and the cost varies with choices. Key elements and cost factors include:

- Benchmark – number of locations
- Training – number of people, locations, duration
- Philosophy – development and complexity
- Rationalization – scope, preparation, methodology, tools, facilitation
- Implementation – scope of changes
- Monitoring – scope, software, architecture
- Continuous improvement – methodology

Consider this example: The company ACME Chemicals is planning an alarm management program.

SCOPE:

- three similar plants: one in Ohio, U.S., one in Northern Ireland (NI), one in China
- about 3,000 tags per site and about 4,500 alarms per site

TRAINING:

- Overview training (2 hours) – all operations, maintenance, and technical personnel
- Detail training (16 hours) – selected operators, automation engineers, process engineers

PHILOSOPHY:

- one development workshop (3 days) with trained representatives from each site
- template philosophy document used for all three sites, with some local modifications

RATIONALIZATION:

- export of current alarms used to build potential alarm list
- unit operation rationalization conducted at NI plant
	- two weeks facilitated rationalization
- rationalization reviewed, modified, and adopted at other sites
	- three-day review

IMPLEMENTATION:

- estimate to remove or add 50 percent, about 2,250 alarms
- estimate to modify priority or set point 80 percent, about 3,700 alarms

MONITORING:

- select software for monitoring and assessment
	- includes a master alarm database and rationalization tool
- installation on central server to compare sites

CONTINUOUS IMPROVEMENT:

- biweekly meeting of the alarm team

Based on this rough plan, the cost can be estimated. Excluding employee time and travel, this program might cost about $150K – $200K.

---

![](https://www.isa.org/getmedia/acdec150-6379-41cd-ab2e-e61ce2ed45a8/MA_2020_Cont-Batch-Process-fig2.gif?width=378&height=190&ext=.gif)

Figure 2. Before and after alarm management.

---

#### What is the cost benefit ratio of alarm management?

The benefits of a successful alarm management program are many, but they are also hard to quantify in dollars. The most obvious benefit is for the operator, with reduced stress from alarms and improved response to alarms since they are all meaningful. Alarm management is one of those rare improvement programs that operators actually “like,” because it makes their lives better. Figure 2 is an example of one company’s experience before and after implementing an alarm management program.

Most of the financial benefit comes from avoiding undesired consequences, so the benefit depends on how many avoidable events happen in the plant before implementing alarm management. Using historical data on avoidable plant shutdowns, avoidable off-quality production, and the like, estimate what the reduction in events would be if the operators had a better system to notify them to take action. Do not assume 100 percent reduction, but a reasonable target like 70 percent, and calculate the value.

Every plant is different, because of culture, products, costs, and the like. ACME used the following data:

Operator-preventable events across the three sites:

- Shutdowns: 10 at $500K average
- Off-quality production: about 200K lbs. at $5/lb.
- Incidents: four at about $100K average

The target savings is about $4.5M, giving the alarm management program a very nice return of about 20 times the external cost. How can a plant not afford to implement an alarm management program?

#### How do I start an alarm management program?

There are three typical ways to start an alarm management program:

1. development of an alarm management philosophy,
2. alarm system monitoring, or
3. alarm system benchmark.

The real starting point is training. Then a plan can be developed that best fits the situation. Typically, new facilities start with option 1, with a goal to develop an alarm philosophy and complete rationalization and training before startup. Many existing facilities start with option 2 or 3, which both include a quantification of the current alarm system performance. With option 2, the alarm system monitoring will show the improvement of fixing the most offensive alarms that do not require rationalization. This is sometimes called bad actor resolution.

BUT before you start an alarm management program, you need to become familiar with the road map to alarm management due to its potential regulatory requirements. Purchase ISA-18.2 or IEC 62682. Become familiar with the alarm management life cycle and the requirements for each stage. ISA-18 has developed a number of technical reports (TRs) that go into detail describing how to implement varies stages of the alarm management life cycle. Purchasing these reports or attending an alarm management training course (by a reputable organization that has been involved with the ISA-18.2 or IEC 62682 standards development since their inception) would be beneficial. There are many organizations that can be described as late to the party who have become informational members to simply market that they are members of the standards to sell their services.

Then transition to the three entry points mentioned above. If you need to develop a business case to justify the project, perform an audit of your alarm system to determine the deficiencies and what areas need to be improved. You could also implement a benchmarking and assessment of your facility to determine if your alarm rates are acceptable (figure 3 has some of the key metrics from ISA-18.2). This will allow you to identify bad actors, which you can mitigate to develop data to help support senior leadership sponsorship for an alarm system improvement project. In addition, you can gather information, such as operator survey results, and a benchmarking and assessment report that compares your plant alarm system key performance indicators (KPIs) with ISA-18.2 and IEC 62682 requirements.

---

![](https://www.isa.org/getmedia/2578a1c9-1687-4757-bc0f-a1775921d7b1/MA_2020_Cont-Batch-Process-fig3.gif?width=437&height=151&ext=.gif)

Figure 3. Key metrics from ISA-18.2.

#### When is the alarm management program complete?

As mentioned above, alarm management is a life-cycle approach managing a work process. Asking when the alarm management program is complete is akin to asking if my safety program is complete. Once you have achieved the benefits of a well-managed alarm system, you will wonder how you ever ran the plant without it, as it is a paradigm shift within the culture for an operating plant. This fundamental shift in an organization’s culture will not be easy and is rarely embraced by everyone, but this shift is required to adhere to the alarm management work processes within the standards. Everyone needs to understand that the benefits are real, quantifiable, and achievable, as there are many who have embraced this change in philosophy.

The benefit is improved plant performance through improved operational discipline, which means doing the right thing at the right time, every time. An alarm system that is well managed will notify the operator at the right time, and only the right time, for a specific action. A well-trained operator, or an operator assisted with some guidance from a well-designed alarm system, will know the right action to take in response to the alarm. An operator, not overloaded with alarms, will take the right action at the right time to correct the process condition. These imperatives are clearly and concisely stated by Campbell Brown in his famous “Horses for Courses – A Vision for Alarm Management” paper: “the fundamental goal is that Alarm Systems will be designed, procured and managed so as to deliver the right information, in the right way and at the right time for action by the Control Room Operator (where possible) to avoid, and if not, to minimise, plant upset, asset or environmental damage, and to improve safety.”

M. L. Bransby and J. Jenkinson conclude in their HSE report “The Management of Alarm Systems” that “poor performance costs money in lost production and plant damage and weakens a very important line of defense against hazards to people.” Therefore, improved operational discipline results in fewer incidents, increased plant reliability, reduced quality problems, and reduced environmental excursions and equipment damage. Therefore, like safety, your path to alarm management enlightenment is a continuous process.

#### Is alarm management really just a software application?

NO, alarm management is not just a software application. The software application is the tool utilized to monitor the alarm system. Monitoring an alarm system is essential to ensure that the system is functioning within the defined metrics dictated by your philosophy. If the alarm system is not monitored, it is highly likely that it is outside of these metrics and thus not useful in allowing the operator to respond to the abnormal situation in a timely manner.

#### Is alarm management really just rationalization?

NO, alarm management is not really just about rationalization. Rationalization involves reviewing and justifying potential alarms to ensure that they meet the criteria for being an alarm as defined in the philosophy. It also involves defining the attributes of each alarm (such as limit, priority, classification, and type) as well as documenting the consequence, response time, and operator action. Although safety alarms generally tend to be some of the most critical in a plant, they still must go through the rationalization process. The product of rationalization is a list of configuration requirements recorded in the master alarm database (MAD). Alarm classification and prioritization are extremely important parts of rationalization. They are not mutually exclusive or redundant. Classification is a tool for managing requirements. Prioritization is exclusively for the benefit of the operator.

Alarm management is a process that involves managing alarms through the alarm management life cycle. ISA-18.2 and IEC 62682 are standards that provide a framework for the successful design, implementation, operation, and management of alarm systems in a process plant. They use a life-cycle approach consisting of distinct stages, which are similar in many respects to the life-cycle methodology of the ANSI/ISA-84 Functional Safety Standard. Although the use of life cycle is common to both standards, alarm management is a continuous activity, due to the scale and the processing of all alarms by the operator, requiring ongoing performance evaluation and adjustment. Alarm system performance evaluation or monitoring is one of the essential elements of alarm management.

Monitoring alarm system performance can be used to maintain the integrity of the safety system. In addition, the reliability of an alarm cannot be determined without an understanding of the overall performance of the alarm system. Reports can be generated that document the triggered alarms, indicating that a demand has been placed on a safety instrumented function (SIF). The frequency of layer of protection analysis (LOPA) alarms (alarms that are listed in a layer of protection analysis) can be used to evaluate and validate the assumptions of initiating event frequency. Overall performance has a direct impact on the operator’s ability to successfully respond to individual alarms. An unmonitored alarm system is essentially a poorly performing alarm system that correlates to a broken alarm system.

#### What further information is available on alarm management?

There are dozens of well-written papers by individuals who have been active in ISA-18.2 since the 2003–2005 time frame. These individuals have been involved since the beginning of the journey to develop the first standard on alarm management. In addition, there are several books and courses available to provide further guidance on the topic.

The ISA-18.2 TRs are also a valuable resource, as they provide the guidance on how to implement alarm management. Remember, a standard communicates what you shall or should do, where a TR communicates how to do it.

The authors of this article have included a short list of published papers that provide guidance on alarm management. If you have difficulty finding additional viable resources, the authors have lists of resources we can share.

#### Can I get help to implement my alarm management program?

Yes, you can get help implementing an alarm management program, but as they say, be careful of what you ask, because there may be unintended consequences. Every company that has anything to do with control systems or automation services today markets themselves as “alarm management subject-matter experts.” Most of these organizations have published white papers on the subject, and often this material is poor guidance at best if not completely wrong.

As with any contractor, it is important that you vet the company and individuals who are going to provide alarm management services. At a company where he worked, one of the authors of this article has seen reportable incidents due to poor alarm management rationalization. Essentially, the company, which is well known in the alarm management business, rationalized critical alarms out of existence.

There are numerous resources available, but you must review each to ensure that it will bring value to you and your organization.

#### Reader Feedback

---

We want to hear from you! Please send us your comments and questions about this topic to [InTechmagazine@isa.org](mailto:InTechmagazine@isa.org).

- [Twitter](https://twitter.com/ISA_Interchange)
- [Linked In](http://www.linkedin.com/groups?gid=137598)

#### About The Authors

---

**Donald G. Dunn** is a senior consultant with WS Nelson, providing services to the refining, chemical, and other industries. He is currently a senior member of the IEEE and ISA and is also a member of the NFPA, API, and IEC standards development organizations. He co-chairs ISA18, chairs IEEE841 and 841.1, and is the convener of IEC 62682. Dunn served as the vice president of the ISA Standards and Practices Board in 2011–2012.

---

[**Nicholas P. Sands, PE, CAP**](mailto:Nicholas.P.Sands@USA.dupont.com), is an ISA Fellow, the ISA vice president of standards and practices, and a Manufacturing Technology Fellow at DuPont with more than 25 years of alarm and SIS experience. Sands is co-chair of the ISA18 committee working on alarm management, served as secretary for the IEC 62682 committee, and was involved in the development of the Certified Automation Professional program. He is also an ISA course developer and instructor. Sands’ path to instrumentation and control started when he earned his BS in chemical engineering from Virginia Tech.