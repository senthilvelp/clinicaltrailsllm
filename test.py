from vectors.vector import CTVector

texts = """The purpose of this study is to determine the effectiveness of a physician led,&#xD;
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

embeddings = CTVector(text=texts)
print(embeddings)