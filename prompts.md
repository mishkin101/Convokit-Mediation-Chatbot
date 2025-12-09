# Planning

- Agreement Options:
    - Refund (none / partial / full) (0 , .5, 1)
    - Whether your negative review stays or is dropped (0 or 1)
    - Whether their negative review stays or is dropped (0 or 1)
    - Whether someone apologizes (and who) (0 or 1)

- Impasse:
- constant payoff baseline of 40
- To compute Zopa:
    - Use LLM to get weight of each combination of each agreement type from set of possibilities based on context from pool of 100 points. do for each participant
    - suggest deals where each deal combo is aove impasse baseline.

- Chat interace between buy and seller. 
    Functionality:
    - ability to type messages
    - recieve intervention messages from LLM
- For every message exchange, call convokit model with conversation context up to that point.
    - if derailement threshold reached  1st time, prompt with perspective-taking rephrasing 
    - 2nd time: perspective-taking rephrasing 
    - 3rd time: if escalation keeps increasing, prompt with ZOPA

Mediation Theory:

-ZOPA (zone of possible agreement)
    - 
- Perspective taking re-phrasing: (summary of other, concerns, rephrasing of message.) 
- also restate the intended goal + find possible ZOPA of compromise options
- when 1st derailement detected, prompt with suggestion based on: 
    - https://dl.acm.org/doi/full/10.1145/3613904.3642322
    - this paper creates prompts for LLM based on TKI conflict styles.
    - soft suggestions: on first derailment, offer only perspective taking re-phrasing
    - hard suggestions: if escalation score keeps increasing, offer ZOPA + perspective taking rephrasing


- Need: 
    - ConvoKit interface for derailement model
    - LLM model for mediation

Set-up:

