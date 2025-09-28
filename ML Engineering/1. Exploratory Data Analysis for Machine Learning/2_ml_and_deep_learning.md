# What is Machine Learning (ML)?

*Definition*: Study and construction of programs that **learn patterns from data** instead of being explicitly programmed.
*Key idea*: The more data → the better ML learns patterns (until performance plateaus).
*Not rule-based*: Unlike traditional systems, ML is not programmed with explicit rules.

Features and Target

Features = input variables used for prediction.

Target = output label we want to predict.

Example: Iris Dataset

Features: sepal length, sepal width, petal length, petal width.

Target: species of iris (setosa, versicolor, virginica).

# Types of Machine Learning

1. *Supervised Learning*
* Has labels (target column).
* Goal: Predict labels.
* Examples:
  * Spam detection (spam / not spam).
  * Fraud detection (fraud / not fraud).


2. *Unsupervised Learning*
* No labels.
* Goal: Find hidden structures/patterns.
* Examples:
  * Customer segmentation (group customers by behavior).
  * Market basket analysis.

In unsupervised learning, there’s often no clear “right answer.”



## 5. Features in Different Contexts

### Structured Data

* Features: transaction time, amount, location, purchase category.
* Example: Fraud detection → predict fraud / not fraud.
* ✅ ML works well here.

### Image Data

* Features = pixels (e.g., 256 × 256 → 65k features).
* Issues:

  * Too many features.
  * Spatial relationships between pixels lost.
* ❌ Hard for classical ML.
* ✅ DL can solve this by automatically learning spatial patterns.

---

# Deep Learning (DL)

*Definition*: Subset of ML using **deep neural networks**.
*Key strength*: Learns features automatically from raw data.
*Applications*: Image classification, NLP, speech recognition.



## 7. Classical ML vs. Deep Learning

| Aspect                  | Classical ML                        | Deep Learning                                             |
| ----------------------- | ----------------------------------- | --------------------------------------------------------- |
| **Feature engineering** | Manual (human-designed)             | Automatic (learned by NN)                                 |
| **Data size**           | Performs well on small datasets     | Needs large datasets                                      |
| **Interpretability**    | Easier (features are human-defined) | Harder (features are abstract, hidden)                    |
| **Adaptability**        | Works better with changing data     | Needs retraining, less flexible                           |
| **Performance**         | Strong on structured/tabular data   | Outperforms ML on unstructured data (images, text, audio) |

---

## 8. Summary

* **ML** = learns from data, better with more data.
* **Supervised ML** = prediction from labeled data.
* **Unsupervised ML** = pattern discovery without labels.
* **DL** = powerful subset of ML → automatically learns features, but needs big data.
* In **small, structured datasets**, ML often outperforms DL.
* In **large, unstructured datasets**, DL dominates.



# The Challenge with Images in Traditional ML

* Images as data: stored as pixels (numerical values for color/brightness).
* Example: A **256×256 image = 65,536 pixels → 65,536 features**.
* Problems:
  * Too many features → computationally heavy.
  * Pixels alone lose **spatial relationships** (e.g., eyes vs. nose depend on *relative position*, not just pixel color).
  * Feature engineering (hand-crafting features like edges, textures) is hard and requires expert effort.



# Deep Learning: The Solution

* **Definition**: A subset of Machine Learning that uses **deep neural networks** (multiple layers).
* **Key power**: Learns features **automatically** from raw data.
* Example (image classification):

  * Input: raw pixels.
  * Neural net layers:

    * Early layers detect simple features (edges, corners).
    * Middle layers combine them into shapes (eyes, nose, mouth).
    * Later layers assemble into whole objects (cat, dog, human).
* Removes the need for humans to manually define features.



## 3. When to Use Deep Learning vs. ML

* ✅ **Deep Learning is best when**:

  * You have **large datasets** (images, speech, text).
  * Complex features need to be learned automatically.
* ✅ **Traditional ML is better when**:

  * You have **smaller datasets**.
  * Data is structured (tables, numbers, transactions).
  * Dataset changes rapidly over time (easier retraining).



## 4. Key Difference in Workflow

### Classical Machine Learning:

1. Human defines features manually (e.g., edges, nose, shapes).
2. Model trained on those features.

### Deep Learning:

1. Input raw data (e.g., pixels).
2. Neural network **extracts features automatically**.
3. Learns hierarchical representation (edges → shapes → objects).



## 5. Why It Matters

* Deep Learning = breakthrough → solved problems that ML struggled with (e.g., image classification, speech recognition, machine translation).
* Limitation: requires **big data + big compute** to work well.

