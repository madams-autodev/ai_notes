# 📘 Notes: Machine Learning Workflow & Vocabulary

## 🎯 Learning Goals

* Understand **fundamental ML concepts**.
* Review **basic background knowledge** required:

  * Python libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Keras.
  * Tools: Jupyter / iPython.
  * Math/stat foundations: probability, Bayes’ rule, moments, linear algebra.
* Learn the **ML workflow** from problem to deployment.
* Build vocabulary: **target, features, examples, labels**.

---

## 🔄 Typical Machine Learning Workflow

1. **Problem Statement**

   * Define: *What problem are we solving?*
   * Ex: Image recognition → classify dog breeds.

2. **Data Collection**

   * Gather sufficient & diverse labeled data.
   * Ex: Many pictures of each breed (different angles, lighting).

3. **Exploration & Preprocessing**

   * Inspect + clean data.
   * Ex: Check distributions, heatmaps of pixels, handle missing values.
   * Convert raw inputs (like images) into model-usable formats (arrays, encodings).

4. **Modeling**

   * Build models → start with baseline, iterate to more complex.

5. **Validation**

   * Test on *holdout* (unseen) set.
   * Ex: Did our dog-breed classifier generalize?

6. **Decision & Deployment**

   * If results are strong → communicate to stakeholders, deploy into production.

---

## 📑 Core Vocabulary (Spreadsheet Analogy: *Iris Dataset*)

* **Target Variable** → the value we want to predict.

  * Ex: Flower species (setosa, versicolor, virginica).

* **Features (Explanatory Variables)** → input columns used to predict the target.

  * Ex: Sepal length, sepal width, petal length, petal width.

* **Example / Observation** → a single row in the dataset.

  * Ex: One flower’s measurements + its species.

* **Label** → the actual value of the target variable for one example.

  * Ex: “versicolor” in a row.

---

## ✅ Key Takeaways

* **Workflow**: Problem → Data → Explore/Preprocess → Model → Validate → Deploy.
* **Vocabulary**: Targets (what we predict), Features (what we use), Examples (rows), Labels (target values).
* **Foundations matter**: solid stats + linear algebra prevent misuse of ML models.

---

👉 Want me to also create a **visual one-page diagram of the workflow + vocabulary (like a flowchart with dataset example)** so you can use it as a quick reference sheet?
