# Assessing the relationship between stimulus duration and Mean Opinion Score for speech synthesis evaluation

This repository serves to host files necessary to replicate the research done in my master's thesis. The primary goal of this thesis was to measure the potential effect of speech clip duration on the MOS of synthetic voices of all qualities. This thesis was completed in June 2024 to fulfill the requirements for the degree of Master of Science in Voice Technology at Rijksuniversiteit Groningen - Campus Fryslân.

When the thesis is evaluated and published, the final version of the thesis will be linked here. 

## Table of Contents

- [Abstract](#abstract)
- [Pilot Experiment](#pilot-experiment): Includes all data needed to recreate the pilot experiment.
  - [Participant Selection](#participant-selection)
  - [Stimuli](#stimuli)
  - [Procedure](#procedure)
- [Primary Experiment](#primary-experiment): Includes all data needed to recreate the primary experiment.

## Abstract

Despite the rapid advancements in speech synthesis, the Mean Opinion Score (MOS), established
in the 1990s and relatively unchanged since, remains the standard for evaluating speech synthesis. 
Lack of reassessment of MOS over time has raised many questions about the reliabilty and
robustness of the field’s predominant evaluation metric. Therefore, this study critically assesses how
non-standardized testing variables may affect MOS, using listening tests to measure how four different 
durations of synthetic speech clips interact with the MOS ratings of three different synthetic
voices. While the results show that duration does not have a statistically significant impact on the
MOS of a synthetic voice, therefore producing inconclusive results, there is promise in continued
research as shown by the 33.9% reported effect size. This moderately strong effect size suggests the
possibility of a meaningful association between duration and MOS. Overall, this study highlights
the lack of standardization present in MOS evaluation and the questions the reliability of this 
evaluation metric. It is therefore suggested to continue MOS research on not only duration, but also other
unstandardized variables, as well as the implementation of best practices in MOS testing.

## Pilot Experiment

Prior to the experiment, a pilot test was conducted to assess the suitability of the study, as well as
to offer an opportunity to refine the research design. It additionally served as method to ensure the
reliability of the data collection process with the survey software and identify any potential issues.
Data needed to recreate this experiment can be found [here](https://github.com/branaphy/msc-vt-thesis/tree/main/Pilot%20Experiment).

### Participant Selection

A small sample of 18 participants was selected for the pilot test. Participants were recruited via
word of mouth and social media. There were no inclusion or exclusion criteria set for the selection
of participants. 

### Stimuli

The stimuli for the pilot test were created from two voices. The first voice was a synthetic voice
generated using a pre-trained model of [MMS TTS](https://huggingface.co/facebook/mms-tts-eng). 
The second voice was a human voice, with the recording being provided with consent by a classmate. 
The human voice was not altered in any way outside of being trimmed to fit the varying durations.

### Procedure

Participants were presented with 4 speech clips, each of a unique duration. The clips were presented
in a randomized order to each participant to prevent order effects. Additionally, each participant was
only presented with a clip set from one of the two voices. The voice presented to the participant was
chosen at random, yet distributed evenly. Additionally, participants received, at random, one of two
possible stimuli for the phrase and sentence durations.

Participants were asked to rate the naturalness of each speech sample on a scale of 1 to 5, with 1
representing Bad and 5 representing Excellent. There were no additional labels on the numbers. In
addition, participants were required to rate the speech clips one at a time and were unable to return
to past questions to limit comparison.

## Primary Experiment

Data needed to recreate this experiment can be found [here](https://github.com/branaphy/msc-vt-thesis/tree/main/Primary%20Experiment).

### Participant Selection

Participants were recruited via word of mouth and via social media platforms: Facebook, LinkedIn,
and Instagram. There were no explicit inclusion or exclusion criteria set for participants. A total of
110 participants were recruited for this study.

### Stimuli

The speech clips were created across three different synthetic voices to test how duration affects
MOS across different speech quality levels. The selected voices were chosen by reviewing the
[trending pre-trained models on Hugging Face](https://huggingface.co/models?pipeline_tag=text-to-speech&sort=trending). Two of the chosen voices were created 
using [Parler-TTS Mini: Expresso](https://huggingface.co/parler-tts/parler-tts-mini-expresso). This model offers 4 voices, 2 male and 2 female. Additionally, the model
offers variances in emotion and speaking rate. Manipulating each of these variables allows for the
produced voices to be distinct from each other, despite being generated from the same pre-trained
model. The third chosen voice was created using the [SpeechT5 model](https://huggingface.co/microsoft/speecht5_tts).

### Procedure

Participants were presented with 4 speech clips, each of a unique duration. The clips were presented
in a randomized order to each participant to prevent order effects. Additionally, each participant was
only presented with a clip set from one of the three voices. The voice presented to the participant
was chosen at random, yet distributed evenly.

Participants were asked to rate the naturalness of each speech sample on a scale of 1 to 5. The
answers were labeled with the representation of their perceived naturalness, using the recommenda-
tion from ITU-T Recommendation No. P.800. In addition, participants were required to
rate the speech clips one at a time and were unable to return to past questions to limit comparison.
