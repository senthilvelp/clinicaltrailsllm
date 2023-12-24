from vectors.vector import CTVector

#paragraph = """The research the investigators plan to undertake involves the use of a paper substrate with a gold metamaterial on top or a plastic substrate with gold metamaterial on top in physical contact with paper. The metamaterial has an absorption peak within the terahertz frequency range to be investigated (0.75 - 1.1THz). The serum samples will be soaked into the paper fibres which will shift the absorption peak within the terahertz frequency range dependent on the concentration of tumour markers present in the sample. The serum samples will be surplus from samples tested for CEA, LDH, CA-125, CA 19-9, CA 15-3, total-hCG and AFP at the Durham and Darlington NHS Fondation Trust. The samples will be anonymised with the exception of which tumour marker they were tested for and the level measured. There will be two stages to this research project the initial stage requires 15 samples per proposed marker including 15 samples (across all markers) for negative results. This will be used to identify suitable markers to consider for the second stage. Where 50 to 90 samples of each qualifying marker will be tested dependent on the number required for statistical confidence in stage two with 10 to 18 negative samples required for each qualifying marker, again dependent on the statistical requirements for each marker."""

paragraph = """The purpose of this study is to determine the effectiveness of a physician led,&#xD;
      multi-disciplinary approach to treating obesity that incorporates nutrition (mainly, using&#xD;
      genetics to identify appropriate food intake), exercise, and motivational counseling. We plan&#xD;
      to recruit overweight/obese (BMI&gt;25) males and females to participate. Participants will be&#xD;
      randomized to receive a personalized diet plan, or a standard care diet plan; both groups&#xD;
      will participate in the exercise intervention. For a 6-month duration, both groups will be&#xD;
      asked to improve their diet according to their dietary plan and participate in&#xD;
      moderate-to-vigorous physical activity (gradual increase up to 300 min/week). We intend to&#xD;
      evaluate standard outcomes of weight loss, and assess for any predictors of positive&#xD;
      outcomes. Following the six-month intervention, participants will complete a 3-month no&#xD;
      contact phase. This no contact phase will provide insight into the effects of the study on&#xD;
      weight loss maintenance. Our team also plans to address acceptability by providing&#xD;
      evaluations to study participants and conducting interviews with a small subset of&#xD;
      participants to improve the intervention for the future.&#xD;"""

vectors = CTVector(paragraph)

embeds = vectors.embeddings

print(embeds)