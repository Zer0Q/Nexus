---
title: "Process Automation: Alarm management life cycle"
source: "https://www.isa.org/intech-home/2018/march-april/features/alarm-management-life-cycle?utm_source=chatgpt.com"
author:
published:
created: 2026-05-29
description: "ISA"
tags:
  - "clippings"
summary:
---
### Summary

Fast Forward

- Alarm management concepts are likely well integrated at sites that started with the ASM Consortium work in the 1990s or later with the publication of ISA-18.2 in 2009.
- A common phenomenon of alarm management is an initial gain in performance, followed by a gradual erosion of benefits caused by many variations in operations.
- Life-cycle management is critical for effective long-term operation, and the concept of alarm class helps manage the work process.

##### Leveraging classes

![](https://www.isa.org/getmedia/8fdeab02-74c7-43f5-8e11-d7793a6dcd8b/MA-2018-process-auto-storypg_2.jpg?width=400&height=400&ext=.jpg)

**By Bridget Fitzpatrick**

Alarm systems are critical for facilitating process safety, ensuring efficient operations, and maintaining quality. Alarm management has been broadly implemented in the process industries over the past 20 to 30 years. If your facility has not embraced this fundamental aspect of automation and control, time is wasting! For sites that started in the early days with the ASM Consortium <sup>TM</sup> work of the 1990s, or later with the publication of ISA-18.2 in 2009, alarm management concepts are likely well integrated or even commonplace.

One of the common phenomena of alarm management is an initial gain in performance, followed by a gradual erosion of benefits. A major root cause of this variation is that most processes continually change-perhaps more often than we think. Changes to raw materials and product specifications, debottlenecking, new environmental regulations, and plant trials may affect alarm management. It is important to understand that alarm management is a never-ending effort. Managing the life-cycle aspects is as critical as getting the correct initial design or rationalization. One concept that can help manage the work process is alarm class or classification.

#### What is an "alarm class"?

As stated in ANSI/ISA-18.2-2016, *Management of Alarm Systems for the Process Industries*, an alarm class is a "group of alarms with a common set of alarm management requirements (e.g., testing, training, monitoring, and audit requirements)." One type of alarm class is a safety critical alarm, which, according to ANSI/ISA-18.2-2016, is defined as "an alarm that is classified as critical to process safety for the protection of human life or the environment."

An alarm may belong to more than one class. The alarm philosophy is *required* to provide a definition for alarm classes. However, like requirements in many standards, the specific definition and requirements of alarm classes are left to the owner to define. The recommendation is to embrace the alarm class as a tool in site alarm management work processes to help ensure effective requirement management of special types of alarms. In setting requirements for alarm classes, it can be effective to review the components of the ANSI/ISA-18.2 life cycle (figure 1).

---

![](https://www.isa.org/getmedia/a5296d01-b7a0-4157-99d0-85d9d543383f/MA-2018-process-auto-fig-1.jpg?width=520&height=368&ext=.jpg)

Figure 1. ANSI/ISA-18.2 alarm management life cycle.

Per ANSI/ISA-18.2-2016, specific alarm management considerations should include:

- alarm prioritization
- alarm documentation
- human-machine interface design
- operating procedures associated with these alarms
- operator training and training documentation
- alarm maintenance
- alarm testing
- alarm monitoring and assessment
- alarm management of change
- alarm history retention
- alarm auditing

When alarm management software is actively used to manage the alarm system, an alarm class can be a very effective cross-reference tool. The classification can help manage and record compliance with requirements and help prevent inadvertent deletion of, or changes to, important alarms.

#### Common types of classes

Alarms can come from a variety of sources. The most common classes of alarms are related to personnel protection, safety, product quality, environmental issues, and company or site policies.

Assigning classes of alarms by only the source may seem attractive; however, the alarm source can have a wide variety of alarm management requirements. All functional safety alarms, for example, can have different requirements for training, testing, auditing, or documentation. Class assignment depends on the requirements of the grouped alarms.

#### Highly managed alarms

ANSI/ISA-18.2 introduced the concept of the highly managed alarm (HMA). HMAs by definition require more administration and documentation. If HMA classes are used, the alarm philosophy requires the organization to define the criteria for assigning alarms to HMA classes. The designation of alarm classes as highly managed should be based on essentials, including alarms for:

- process safety that is critical to protecting human life (e.g., safety alarms)
- personnel safety or protection
- environmental protection
- current good manufacturing practice
- commercial loss
- product quality
- process licensor requirements
- company policy

Although this may seem to add paperwork and complexity for limited or no gain, experience has shown it is an effective best practice for managing the requirements.

**Example alarm class: H2S toxic gas**

The detection of hydrogen sulfide gas (H2S) will likely have defined action and danger levels for different physical areas. Managing these alarms as a class defines these settings, special handling based on mode of operation, the human-machine interface (HMI) presentation, operator response, frequency of testing, training for staff, metrics for monitoring and reporting, and audit requirements.

A problematic H2S monitor that routinely alarms might have its alarm set point raised to not report the "nuisance" spike. Masking that spike might hide a safety concern related to a routine spike of detected H2S during a sampling procedure. A managed H2S class alarm will detect that change during an audit, recognize the sampling procedure issues, and result in a safer condition.

**Steps for an effective alarm system**

Falling back on the old adage that you cannot improve what you do not measure, monitoring, assessment, and audit activities are arguably the most important for long-term success. By undertaking monitoring and assessment, actual performance is measured and available for improvement. Similarly, audits of the work processes highlight any behavior that does not follow the alarm philosophy.

Note: The ISA technical report on this topic (ISA-TR18.2.5-2012, *Alarm System Monitoring, Assessment, and Auditing*) is a good reference for methods, metrics, and work practices.

The three loops shown in the ISA life cycle (figure 1) highlight areas for focused activity: audit and philosophy, monitoring and management of change, and monitoring and maintenance.

- An audit is conducted to ensure that the alarm management work processes are sound and aligned with the philosophy. As alarm management work processes mature, it is important to make sure that the philosophy is updated to reflect changes in practice. Philosophy documents that remain out of sync will fall increasingly out of use.
- In monitoring performance, issues related to following management of change procedures will become apparent. To effectively manage alarm systems, it is common to develop "fast track" or simplified processes. Allowing changes to occur without following a formal management of change process will make it difficult to achieve system integrity.
- Similarly, allowing the maintenance function to transfer alarms in and out of service without structured expectations and schedules can cause less effective systems.

#### Manage the work processes

Alarm class can help manage each stage of the life cycle:

*Philosophy*: In the philosophy process, operational definitions or terms and work processes are set. Alarm classes are listed and defined. This establishes clear expectations about alarm classes and how their related requirements are managed throughout the life cycle.

*Identification*: In a similar manner, clear alarm class ground rules set in the work practices related to identification help manage consistency.

*Rationalization*: Guidelines related to different classes of alarms help streamline and manage the rationalization process. Classes are assigned during rationalization.

*Detailed design*: Alarm classes may have specific requirements for setting the alarm design basis. This may be related to things such as the alarm limit or priority, implementation details, the general presentation on the HMI, or the need for specific online help information.

*Implementation*: When implementing certain alarm classes, specific requirements for testing and training may be required.

*Operation*: When certain alarm classes are in operation, they require refresher training.

*Maintenance*: Taking certain alarm classes out of operation and placing them into the maintenance stage of the life cycle may require specific remediation plans. Additional monitoring requirements, altered modes of operation, or specific testing requirements might be needed before returning to service.

*Monitoring and assessment*: An emerging concept requires the alarm system as a whole to meet certain performance levels to continue to take credit for independent protection layer (IPL) alarms.

**Example alarm class: IPL alarms**

A layer of protection analysis may identify alarms that provide risk reduction. These are generally known as independent protection layer alarms. Such alarms may have additional requirements for monitoring, including frequency, time in alarm, time shelved, time out of service, average alarm rate when active, and percent of time participating in an alarm flood.

"High frequency" may indicate time durations higher than estimated during the functional safety studies. "Time in alarm" may reflect exposure time to the underlying hazard. "Shelved" and "out of service time" may reflect time not available as a layer of protection. Review of these time frames in an audit may reflect the need for recognition of different modes of operation, addition of alternate alarms, and related recordkeeping

*Management of change*: Alarms generated from engineering studies or functional safety may require different levels of approval for changes.

*Audit*: Certain classes of alarms may require specific audit periods or level of detail on audits to meet compliance requirements.

#### Right size the effort

Adding alarm classes may seem daunting at first. However, managing the requirements is much easier to implement if you recognize that some alarm types have different life-cycle requirements. Segregate those alarms into classes as a first phase. To "right size" the effort, use an initial approach of generating a set of alarm classes that splits out the key "special" or HMA alarms and leaves the rest as a general class. It is important to approach the process by finding the important alarms with special requirements, rather than considering the need to discuss and classify every alarm.

#### Reader Feedback

---

We want to hear from you! Please send us your comments and questions about this topic to [InTechmagazine@isa.org](mailto:InTechmagazine@isa.org).

- [Twitter](https://twitter.com/ISA_Interchange)
- [Linked In](http://www.linkedin.com/groups?gid=137598)

#### About The Authors

---

**[Bridget Fitzpatrick](mailto:Bridget.Fitzpatrick@woodplc.com),** an ISA Fellow, is disciple technical authority for HMI, abnormal condition management and human factors, for the automation and control organization within Wood. Wood provides project, engineering, and technical services for energy and industrial markets. Fitzpatrick has an MBA in technology management from the University of Phoenix and a SB in chemical engineering from the Massachusetts Institute of Technology. She sits on the ISA Standards and Practices Board and is managing director of the ISA18 (Alarm Management) committee.