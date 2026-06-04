# Missing Images Analysis for ux-fr.com

Analysis date: 2026-06-03.

Source of truth used:

- Current WordPress site API: `https://ux-fr.com/wp-json/wp/v2`
- Local migration report: `migration-report.json`
- Direct network checks against original and candidate replacement URLs

The migration detected 31 failed asset URLs. Not all of them are real content
images: 3 are document links and 3 are Amazon affiliate tracking pixels. The
current migration therefore overuses the generic placeholder in a few places
where the better fix is to remove the image or restore a plain link.

## Summary

- Real missing image URLs: 25
- Non-image document links: 3
- Amazon tracking pixels: 3
- Verified direct replacements found: 4
- Internet Archive replacement confirmed: 1
- Images probably requiring manual replacement/redraw: 13+

## Recommended Global Fixes

1. Remove Amazon `assoc-amazon.fr/e/ir` tracking pixels from migrated content.
   They are invisible analytics beacons, not article images.
2. Do not replace broken PDFs with the image placeholder. Keep them as text
   links, update them to stable document URLs, or remove them if the source is
   not recoverable.
3. Prefer local copies under `static/wp-content/uploads/recovered/` once a
   replacement is found, so the Hugo site does not depend on third-party hosts.
4. For old Google Docs image URLs, treat the exact images as lost unless they
   can be recovered from a private backup or Wayback snapshot.

## Per-Asset Findings

| # | Source page | Missing asset | Problem | Recommended solution |
|---|---|---|---|---|
| 1 | [Soiree Product Tank](https://ux-fr.com/2013/07/05/soiree-du-product-tank-paris-autour-de-lexperience-utilisateur/) | `faculty.washington.edu/.../Medlock2005RITE.pdf` | Not an image. The URL now returns HTML instead of a PDF. | Restore as a text link only. Find a stable copy of the RITE paper manually before downloading locally. |
| 2 | [Nouveau site Transilien](https://ux-fr.com/2012/11/27/lexperience-utilisateur-du-nouveau-site-transilien/) | `assoc-amazon.fr/e/ir?...2212134061` | Amazon affiliate tracking pixel, not content. | Remove the placeholder image. Keep the visible Amazon book/product link. |
| 3 | [Journee Design UX](https://ux-fr.com/2012/09/12/journee-design-experience-utilisateur-a-la-cantine-par-sylvie-daumal/) | `Business_Model_Canvas.png/800px...` | Wikimedia old thumbnail URL now returns HTTP 400. | Use verified original: `https://upload.wikimedia.org/wikipedia/commons/1/10/Business_Model_Canvas.png`, then store locally. |
| 4 | [Emotions design - en pratique](https://ux-fr.com/2012/04/30/les-emotions-dans-le-design-en-pratique/) | `assoc-amazon.fr/e/ir?...2212133987` | Amazon affiliate tracking pixel, not content. | Remove the placeholder image. Keep the visible Amazon book/product link. |
| 5 | [Emotions design - en pratique](https://ux-fr.com/2012/04/30/les-emotions-dans-le-design-en-pratique/) | `assoc-amazon.fr/e/ir?...2804165701` | Amazon affiliate tracking pixel, not content. | Remove the placeholder image. Keep the visible Amazon book/product link. |
| 6 | [Service Design Thinking 1](https://ux-fr.com/2011/09/12/this-is-service-design-thinking-1ere-partie/) | `pixelpinch.com/.../innowiz-project-user-centred-design.jpg` | Source host closes the connection; old blog/media path likely gone. | Search Wayback or replace with a new local user-centred-design illustration. |
| 7 | [La proximite](https://ux-fr.com/2010/09/15/la-proximite/) | `Gestalt_proximity.svg/200px...png` | Wikimedia old thumbnail URL now returns HTTP 400. | Use the original Commons SVG `https://upload.wikimedia.org/wikipedia/commons/2/22/Gestalt_proximity.svg` or download from the Commons file page, then store locally. |
| 8 | [Notes sur iPhone](https://ux-fr.com/2010/09/10/application-notes-sur-iphone-pourquoi-apple-a-tout-faux/) | `static.ispot.co.il/.../bumptop.jpg` | Host no longer resolves. No Wayback copy found during this run. | Replace manually with a local screenshot/illustration of BumpTop or remove image if not essential. |
| 9 | [Hierarchie des besoins](https://ux-fr.com/2010/08/23/la-hierarchie-des-besoins/) | `media.smashingmagazine.com/.../design-hierarchy-of-needs.png` | Old Smashing CDN host no longer resolves. | Use verified replacement: `https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/b4cfd769-b40e-4696-87e6-ced1987749ac/design-hierarchy-of-needs.png`, then store locally. |
| 10 | [Forme suit la fonction](https://ux-fr.com/2010/08/17/la-forme-suit-la-fonction/) | `media.smashingmagazine.com/.../google-home-page-2.jpg` | Old Smashing CDN host no longer resolves. | Use verified replacement: `https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/ee58b839-eb91-487b-9c40-85b7b9fd2e85/google-home-page-2.jpg`, then store locally. |
| 11 | [Loi de Fitts](https://ux-fr.com/2010/08/03/la-loi-de-fitts/) | `pii.tls.cena.fr/docs/NR97-621.pdf` | Not an image. Host no longer resolves. | Restore as a text link or replace with a stable Fitts' law reference. Do not show an image placeholder. |
| 12 | [Boucle de feedback](https://ux-fr.com/2010/08/02/la-boucle-de-feedback-ou-retroaction/) | `gerrymarten.com/.../02-5-english.gif` | URL returns HTML instead of image. | Search Wayback; if not recoverable, replace with a locally redrawn positive-feedback/population diagram. |
| 13 | [Boucle de feedback](https://ux-fr.com/2010/08/02/la-boucle-de-feedback-ou-retroaction/) | `slashgear.com/.../segway.jpg` | URL returns HTML instead of image. | Replace with a local Segway/feedback illustration or find a licensed equivalent. |
| 14 | [Chemin desire](https://ux-fr.com/2010/07/05/chemin-desire/) | `computerparkindia.com/microsoft_keyboard.jpg` | HTTP 404. | Replace with a local photo of a Microsoft ergonomic keyboard or remove if decorative. |
| 15 | [Chemin desire](https://ux-fr.com/2010/07/05/chemin-desire/) | `khayspace.info/.../eyetracking_shoppingcart.png` | Response is empty/tiny; image unavailable. | Search Wayback; otherwise replace with a local eye-tracking/e-commerce heatmap illustration. |
| 16 | [Controle](https://ux-fr.com/2010/06/28/controle/) | `your-translations.com/images/dialog customize.jpg` | HTTP 404. | Replace with a local screenshot illustrating Word customization/control. |
| 17 | [Destin commun](https://ux-fr.com/2010/06/24/destin-commun/) | `bluelarix.com/.../radar_image.jpg` | HTTP 403 forbidden. No Wayback copy found during this run. | Replace with a local radar/grouped-motion illustration. |
| 18 | [La consistance](https://ux-fr.com/2010/06/04/la-consistance/) | `technestreport.com/.../os_x_interface_consistency.jpg` | Host no longer resolves. | Search Wayback or replace with a local Mac OS consistency screenshot/illustration. |
| 19 | [Formes anthropomorphiques](https://ux-fr.com/2010/06/01/formes-anthropomorphiques/) | `upload.wikimedia.org/wikipedia/en/9/9c/1915_proto_hiRes.jpg` | HTTP 404; old Wikimedia file path likely removed or renamed. | Search the Wikimedia file page for the Coca-Cola 1915 prototype image; if unavailable, use a licensed equivalent or remove. |
| 20 | [Formes anthropomorphiques](https://ux-fr.com/2010/06/01/formes-anthropomorphiques/) | `uncrate.com/.../method-dish-soap.jpg` | HTTP 404 on source site. | Use confirmed Wayback copy `https://web.archive.org/web/20091024212308id_/http://www.uncrate.com/men/images/method-dish-soap.jpg`, then store locally. |
| 21 | [Affordance](https://ux-fr.com/2010/05/29/affordance/) | `iqcontent.com/.../push door jpeg small.jpg` | HTTP 404. | Search Wayback; otherwise replace with a local push-door/affordance photo. |
| 22 | [Esthetisme](https://ux-fr.com/2010/05/28/esthetisme/) | `mac4ever.com/.../iphone_nano...jpg` | HTTP 410 Gone. | Replace with a local historical iPhone/iPod rumor image only if licensing is clear; otherwise remove. |
| 23 | [Accessibilite](https://ux-fr.com/2010/05/26/accessibilite/) | `brailleliga.be/.../ascenseur_32.jpg` | Source timed out; no Wayback copy found during this run. | Replace with a local accessible elevator controls image. |
| 24 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_73gjg297c5_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise redraw the diagram described by title: “Les etapes d'une action pour l'ergonomie”. |
| 25 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_71gr7hgfd2_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise remove or redraw based on article context. |
| 26 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_72hm26rzvx_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise remove or redraw based on article context. |
| 27 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_75hr6p6wf3_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise remove or redraw based on article context. |
| 28 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_76dmsxxdfx_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise remove or redraw based on article context. |
| 29 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_74fw94rzdf_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise remove or redraw based on article context. |
| 30 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `docs.google.com/File?id=dhpnv7mt_77ccrndrc6_b` | Old Google Docs file hosting URL returns 404. | Recover from backup/Wayback if possible; otherwise remove or redraw based on article context. |
| 31 | [Design of Everyday Things resume](https://ux-fr.com/2010/05/13/resume-du-design-of-every-day-things-de-donald-norman/) | `pioneer.netserv.chula.ac.th/.../Design of Everyday Things.pdf` | Not an image. HTTP 404. | Remove the placeholder and replace with a bibliographic reference or publisher/book link; avoid hosting questionable PDF copies. |

## Highest-Impact Fixes To Apply First

1. Replace the two broken Wikimedia images with local copies from their original
   Commons files.
2. Replace the two Smashing Magazine images with verified `archive.smashing.media`
   URLs and store them locally.
3. Remove Amazon tracking placeholders from the three emotions/Transilien posts.
4. Convert broken PDF placeholders back to text links or stable references.
5. For the seven Google Docs images in the Donald Norman article, decide between
   backup recovery, manual redrawing, or removal; these are the least recoverable
   from public web evidence.
