# Missing Images Resolution

Resolution date: 2026-06-04.

Scope: this pass fixes placeholders already present in the migrated Hugo
content. It does not change `scripts/migrate_wordpress.py`.

## Summary

- Placeholder images remaining in `content/`: 0.
- Amazon affiliate tracking pixels kept as images: 0.
- Verified images recovered locally: 5.
- Stable document links restored: 2.
- Pedagogical replacements redrawn as local SVG: 18.

All new assets live under `static/wp-content/uploads/recovered/` and are
referenced from Markdown as `/wp-content/uploads/recovered/...`.

## Resolution Table

| Classification | Affected content | Resolution |
|---|---|---|
| recover | Business Model Canvas article, original placeholder line 18 | Downloaded Wikimedia Commons PNG locally as `business-model-canvas.png`. |
| recover | La proximite, original placeholder line 16 | Downloaded Wikimedia Commons SVG locally as `gestalt-proximity.svg`. |
| recover | La hierarchie des besoins, original placeholder line 26 | Downloaded verified Smashing Magazine asset as `design-hierarchy-of-needs.png`. |
| recover | La forme suit la fonction, original placeholder line 30 | Downloaded verified Smashing Magazine asset as `google-home-page-2.jpg`. |
| recover | Formes anthropomorphiques, Method placeholder line 20 | Downloaded Wayback image as `method-dish-soap.jpg`. |
| remove | Transilien, original placeholder line 30 | Removed Amazon tracking pixel placeholder. |
| remove | Three "emotions dans le design" posts, original placeholder lines 14/18 | Removed Amazon tracking pixel placeholders, kept visible book links. |
| document | Product Tank, original placeholder line 31 | Restored local `rite-method.pdf` link. |
| document | Loi de Fitts, original placeholder line 26 | Replaced dead PDF-image placeholder with DOI reference link. |
| document | Norman summary, original placeholder line 349 | Replaced questionable PDF placeholder with a bibliographic book reference link. |
| redraw | Affordance, original placeholder line 14 | Created `affordance-push-door.svg`. |
| redraw | Chemin desire, original placeholder lines 22 and 28 | Created `ergonomic-keyboard.svg` and `eye-tracking-heatmap.svg`. |
| redraw | Service Design Thinking, original placeholder line 26 | Created `user-centred-design.svg`. |
| redraw | Feedback loop, original placeholder lines 20 and 26 | Created `feedback-positive-population.svg` and `feedback-negative-balance.svg`. |
| redraw | Controle, original placeholder line 22 | Created `word-customization-control.svg`. |
| redraw | Destin commun, original placeholder line 20 | Created `common-fate-radar.svg`. |
| redraw | La consistance, original placeholder line 21 | Created `interface-consistency.svg`. |
| redraw | Formes anthropomorphiques, Coca-Cola placeholder line 17 | Created `anthropomorphic-bottle-abstract.svg`. |
| redraw | Esthetisme, original placeholder line 14 | Created `aesthetic-product-appeal.svg`. |
| redraw | Accessibilite, original placeholder line 14 | Created `accessible-elevator-controls.svg`. |
| redraw | Notes sur iPhone, original placeholder line 70 | Created `bumptop-gravity-metaphor.svg`. |
| redraw | Norman summary, original placeholder lines 68, 132, 158, 160, 165, 309 | Created five Norman diagrams and removed one redundant empty placeholder. |

## Research Notes for Redrawn Images

### Affordance: Door Handle

- Affected post: `content/posts/2010-05-29-affordance.md`, original placeholder
  line 14.
- Original alt/title/caption: "Une porte avec une poginee devant etre poussee".
- Article intent: show the classic contradiction between a handle that visually
  invites pulling and a door that must be pushed.
- Concept summary: perceived affordances and signifiers help a user know what
  action is possible; misleading cues create errors.
- Sources consulted: the migrated article itself; Donald A. Norman, *The Design
  of Everyday Things*; Interaction Design Foundation on affordances
  (`https://www.interaction-design.org/literature/topics/affordances`);
  Wikipedia, The Design of Everyday Things
  (`https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things`).
- Visual requirements: neutral door, clear "POUSSER" label, handle cue shown as
  misleading, no copyrighted product or logo.
- Final solution: `affordance-push-door.svg`, a sober door/control mismatch
  diagram.

### Chemin Desire: Ergonomic Keyboard

- Affected post: `content/posts/2010-07-05-chemin-desire.md`, original
  placeholder line 22.
- Original alt/title/caption: "Clavier ergonomique de Microsoft".
- Article intent: illustrate a product shaped by observed desire paths and body
  posture rather than by an arbitrary rectangular grid.
- Concept summary: ergonomics adapts the artifact to repeated human movement;
  the split keyboard is a practical example of adjusting the interface to wrist
  angle.
- Sources consulted: the migrated article itself; Wikipedia on ergonomics
  (`https://en.wikipedia.org/wiki/Ergonomics`); Fitts' law context for motor
  action in interfaces (`https://en.wikipedia.org/wiki/Fitts%27s_law`);
  Universal Principles of Design, desire lines and ergonomics concepts.
- Visual requirements: avoid Microsoft trade dress, show split key groups and
  wrist angle.
- Final solution: `ergonomic-keyboard.svg`, a generic split keyboard diagram.

### Chemin Desire: Eye Tracking

- Affected post: `content/posts/2010-07-05-chemin-desire.md`, original
  placeholder line 28.
- Original alt/title/caption: "Eye Tracking d'un site e-commerce".
- Article intent: show that observation of actual attention can reveal paths
  users take through an interface.
- Concept summary: eye-tracking heatmaps aggregate fixations and attention
  intensity; they are diagnostic evidence, not a complete usability answer.
- Sources consulted: the migrated article itself; Nielsen Norman Group report
  reference "How to Conduct Eyetracking Studies"
  (`https://media.nngroup.com/media/reports/free/How_to_Conduct_Eyetracking_Studies.pdf`);
  NN/g eye-tracking research summaries; Wikipedia on eye tracking
  (`https://en.wikipedia.org/wiki/Eye_tracking`).
- Visual requirements: generic e-commerce layout, heatmap overlay, no real
  brand page or product image.
- Final solution: `eye-tracking-heatmap.svg`, a local abstract e-commerce
  heatmap.

### User-Centred Design

- Affected post:
  `content/posts/2011-09-12-this-is-service-design-thinking-1ere-partie.md`,
  original placeholder line 26.
- Original alt/title/caption: "Design centre sur l'utilisateur".
- Article intent: support service-design thinking with the user at the centre of
  discovery, ideation, prototyping, and iteration.
- Concept summary: user-centred design keeps user evidence and feedback in the
  design loop instead of treating design as a one-way specification activity.
- Sources consulted: the migrated article itself; ISO 9241-210 human-centred
  design reference; Nielsen Norman Group on user-centered design
  (`https://www.nngroup.com/articles/user-centered-design/`);
  Interaction Design Foundation on human-centered design.
- Visual requirements: circular process, user at centre, French labels, no
  Visual.ly graphic reuse.
- Final solution: `user-centred-design.svg`.

### Feedback Loop: Positive Population Growth

- Affected post:
  `content/posts/2010-08-02-la-boucle-de-feedback-ou-retroaction.md`,
  original placeholder line 20.
- Original alt/title/caption: "Feedback positif sur la population".
- Article intent: explain reinforcement, where a system output increases the
  next input and amplifies the trend.
- Concept summary: positive feedback is a reinforcing loop; in population
  examples, more population can produce more births, which then increases
  population again.
- Sources consulted: the migrated article itself; Universal Principles of
  Design, feedback loop principle; Wikipedia on positive feedback
  (`https://en.wikipedia.org/wiki/Positive_feedback`); Smashing Magazine article
  on designing feedback loops.
- Visual requirements: obvious loop, population/birth relation, not a biological
  model with misleading precision.
- Final solution: `feedback-positive-population.svg`.

### Feedback Loop: Negative Balance Control

- Affected post:
  `content/posts/2010-08-02-la-boucle-de-feedback-ou-retroaction.md`,
  original placeholder line 26.
- Original alt/title/caption: "Le segway utilise un feedback negatif pour
  maintenir l'equilibre".
- Article intent: show stabilizing feedback around an equilibrium point.
- Concept summary: negative feedback compares actual state to target state and
  applies a correction that reduces the error.
- Sources consulted: the migrated article itself; Wikipedia on negative feedback
  (`https://en.wikipedia.org/wiki/Negative_feedback`); control-system feedback
  concepts; Universal Principles of Design.
- Visual requirements: abstract balance controller, no Segway product image or
  trademarked design.
- Final solution: `feedback-negative-balance.svg`.

### Controle: Customization of Word

- Affected post: `content/posts/2010-06-28-controle.md`, original placeholder
  line 22.
- Original alt/title/caption: "Personalisation de Word".
- Article intent: illustrate perceived control through customization options.
- Concept summary: control in interaction design is reinforced by reversible
  actions, visible options, and user choice over the interface.
- Sources consulted: the migrated article itself; Universal Principles of
  Design, control principle; Nielsen Norman Group on user control and freedom
  heuristics (`https://www.nngroup.com/articles/ten-usability-heuristics/`).
- Visual requirements: generic document app, no Microsoft UI screenshot.
- Final solution: `word-customization-control.svg`.

### Destin Commun: Radar Grouping

- Affected post: `content/posts/2010-06-24-destin-commun.md`, original
  placeholder line 20.
- Original alt/title/caption: "Utilisation du principe du destin commun dans les
  radars".
- Article intent: show how objects moving together are perceived as related.
- Concept summary: the Gestalt principle of common fate groups elements with a
  shared movement or trajectory, often more strongly than static proximity.
- Sources consulted: the migrated article itself; Scholarpedia Gestalt
  principles (`https://www.scholarpedia.org/article/Gestalt_principles`);
  ScienceDirect overview of common fate; Wikipedia principles of grouping
  (`https://en.wikipedia.org/wiki/Principles_of_grouping`).
- Visual requirements: radar-like field, grouped trajectories, no military or
  proprietary radar screenshot.
- Final solution: `common-fate-radar.svg`.

### Consistance: Interface Consistency

- Affected post: `content/posts/2010-06-04-la-consistance.md`, original
  placeholder line 21.
- Original alt/title/caption: "MacOS et consistance de l'interface".
- Article intent: show consistent controls and repeated visual patterns across
  windows.
- Concept summary: consistency lowers learning cost because similar actions and
  controls behave the same way across contexts.
- Sources consulted: the migrated article itself; Nielsen Norman Group usability
  heuristic "Consistency and standards"
  (`https://www.nngroup.com/articles/ten-usability-heuristics/`);
  Apple Human Interface Guidelines as design-system context.
- Visual requirements: generic windows with repeated controls, no Mac OS
  screenshot or Apple trade dress.
- Final solution: `interface-consistency.svg`.

### Anthropomorphic Bottle

- Affected post: `content/posts/2010-06-01-formes-anthropomorphiques.md`,
  original placeholder line 17.
- Original alt/title/caption: "Les formes anthropomorphiques de la bouteille de
  Coca Cola de 1915".
- Article intent: explain how product silhouettes can evoke human/body forms.
- Concept summary: anthropomorphic abstraction can trigger affective
  associations without requiring a literal human figure.
- Sources consulted: the migrated article itself; Universal Principles of
  Design, anthropomorphic form; Wikipedia on the contour bottle history
  (`https://en.wikipedia.org/wiki/Coca-Cola_Contour_Bottle`); general
  anthropomorphism reference (`https://en.wikipedia.org/wiki/Anthropomorphism`).
- Visual requirements: no Coca-Cola logo or protected bottle trade dress; keep
  the idea of curved human-like proportions.
- Final solution: `anthropomorphic-bottle-abstract.svg`.

### Esthetisme: Aesthetic Usability Effect

- Affected post: `content/posts/2010-05-28-esthetisme.md`, original placeholder
  line 14.
- Original alt/title/caption: "L'esthetisme et Apple".
- Article intent: discuss aesthetic appeal as part of perceived usability and
  emotional response.
- Concept summary: attractive designs are often perceived as easier to use,
  especially at first contact, but the replacement should avoid a brand-specific
  rumor/product image.
- Sources consulted: the migrated article itself; Universal Principles of
  Design, aesthetic-usability effect; Nielsen Norman Group on aesthetic and
  minimalist design; Wikipedia on aesthetic-usability effect
  (`https://en.wikipedia.org/wiki/Aesthetic-usability_effect`).
- Visual requirements: neutral product cards comparing plain and polished
  presentation; no Apple logo or device copy.
- Final solution: `aesthetic-product-appeal.svg`.

### Accessibilite: Elevator Controls

- Affected post: `content/posts/2010-05-26-accessibilite.md`, original
  placeholder line 14.
- Original alt/title/caption: "Les controles de les controles d'ascenseur sont
  accessibles : informations sonores, visuelles et tactiles".
- Article intent: show multimodal accessibility through visual, tactile, and
  audible information on elevator controls.
- Concept summary: accessible controls need reachable placement plus redundant
  sensory cues, including tactile labels and visual/audible feedback.
- Sources consulted: the migrated article itself; W3C WAI accessibility
  standards (`https://www.w3.org/WAI/standards-guidelines/`); ISO/EN elevator
  accessibility summaries; universal design principles.
- Visual requirements: panel with visual indicator, Braille-like tactile dots,
  sound cue, reachable height, French labels.
- Final solution: `accessible-elevator-controls.svg`.

### Notes sur iPhone: BumpTop Gravity Metaphor

- Affected post:
  `content/posts/2010-09-10-application-notes-sur-iphone-pourquoi-apple-a-tout-faux.md`,
  original placeholder line 70.
- Original alt/title/caption: empty image, article text names BumpTop and
  gravity.
- Article intent: criticize a skeuomorphic metaphor that imports physical
  gravity into a desktop interface.
- Concept summary: metaphors help transfer knowledge, but over-literal physical
  metaphors can add constraints that make digital interaction harder.
- Sources consulted: the migrated article itself; archived/general descriptions
  of BumpTop; Wikipedia on BumpTop (`https://en.wikipedia.org/wiki/BumpTop`);
  Donald Norman on conceptual models and visibility.
- Visual requirements: desktop papers sliding down under gravity, no BumpTop
  screenshot or logo.
- Final solution: `bumptop-gravity-metaphor.svg`.

### Norman: Seven Stages of Action

- Affected post:
  `content/posts/2010-05-13-resume-du-design-of-every-day-things-de-donald-norman.md`,
  original placeholder line 68.
- Original alt/title/caption: "Les etapes d'une action pour l'ergonomie".
- Article intent: visualize the seven-stage action cycle, including execution
  and evaluation.
- Concept summary: Norman's action cycle moves from goal to intention, action
  specification, execution, perception, interpretation, and evaluation.
- Sources consulted: the migrated article itself; Donald A. Norman, *The Design
  of Everyday Things*; Wikipedia theory of action
  (`https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_l%27action_%28Norman%29`);
  Oxford HCI overview of Norman's model.
- Visual requirements: French labels, two halves for execution/evaluation, show
  the two gulfs without copying a published diagram.
- Final solution: `norman-seven-stages-action.svg`.

### Norman: Stovetop Mapping

- Affected post:
  `content/posts/2010-05-13-resume-du-design-of-every-day-things-de-donald-norman.md`,
  original placeholder line 132.
- Original alt/title/caption: two empty images after a paragraph comparing
  stovetop control layouts.
- Article intent: compare poor linear controls with a spatially matched control
  layout.
- Concept summary: natural mapping reduces memory load by making the relation
  between control and effect visible.
- Sources consulted: the migrated article itself; Donald A. Norman, *The Design
  of Everyday Things*; Nielsen Norman Group usability heuristics on match
  between system and real world; archived references to mapping of controls.
- Visual requirements: side-by-side "mapping faible" and "mapping naturel";
  generic stovetop controls.
- Final solution: `norman-stovetop-mapping.svg`.

### Norman: Door and Button Codes

- Affected post:
  `content/posts/2010-05-13-resume-du-design-of-every-day-things-de-donald-norman.md`,
  original placeholder lines 158 and 160.
- Original alt/title/caption: empty images after "Norman's door" and buttons.
- Article intent: show affordance/signifiers for doors and grouping/shape codes
  for controls.
- Concept summary: visible affordances, constraints, grouping, and shape coding
  reduce the number of possible actions a user must consider.
- Sources consulted: the migrated article itself; Donald A. Norman, *The Design
  of Everyday Things*; Interaction Design Foundation on affordances; Gestalt
  grouping references for button grouping.
- Visual requirements: combine the two lost examples into one educational image,
  avoid product screenshots.
- Final solution: `norman-buttons-and-controls.svg`; one duplicate empty
  placeholder was removed.

### Norman: Light Switch Mapping

- Affected post:
  `content/posts/2010-05-13-resume-du-design-of-every-day-things-de-donald-norman.md`,
  original placeholder line 165.
- Original alt/title/caption: empty image after the text on matching light zones
  with switches.
- Article intent: demonstrate why 2D-to-2D spatial correspondence is clearer
  than a one-dimensional row of switches.
- Concept summary: natural mapping turns arbitrary learning into perceptual
  recognition.
- Sources consulted: the migrated article itself; Donald A. Norman, *The Design
  of Everyday Things*; Nielsen Norman Group heuristic "match between system and
  the real world".
- Visual requirements: show four light zones and corresponding switches with
  arrows.
- Final solution: `norman-light-switch-mapping.svg`.

### Norman: Conceptual Models

- Affected post:
  `content/posts/2010-05-13-resume-du-design-of-every-day-things-de-donald-norman.md`,
  original placeholder line 309.
- Original alt/title/caption: empty image after the description of designer
  model, user model, and system image.
- Article intent: show the relationship between designer intent, the presented
  system image, and the user's mental model.
- Concept summary: users do not access the designer's model directly; they infer
  it from the system image, feedback, operations, labels, and documentation.
- Sources consulted: the migrated article itself; Donald A. Norman, *The Design
  of Everyday Things*; Nielsen Norman Group on mental models
  (`https://www.nngroup.com/articles/mental-models/`); Wikipedia on mental
  models (`https://en.wikipedia.org/wiki/Mental_model`).
- Visual requirements: three labeled boxes, mediation through system image,
  French labels.
- Final solution: `norman-conceptual-models.svg`.

## Notes on Recovered Assets

- Wikimedia Business Model Canvas and Gestalt proximity assets were recovered
  from durable Commons originals and stored locally.
- Smashing Magazine assets were recovered from `archive.smashing.media`, not
  hotlinked in content.
- The Method soap image was recovered through Internet Archive using a direct
  archived image URL.
- The RITE PDF was downloaded locally from a still-available copy. Broken PDF
  placeholders that were not legitimate images are now plain links.
