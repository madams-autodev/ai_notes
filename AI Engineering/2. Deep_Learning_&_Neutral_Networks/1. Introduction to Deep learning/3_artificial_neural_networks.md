# Artificial Neural Networks (ANNs)

## 1. 🔑 What is an Artificial Neuron?

* An **artificial neuron** = also called a **perceptron**.
* Inspired by **biological neurons**.
* Works by:

  1. Taking **inputs** (`x1, x2, ...`).
  2. Multiplying each input by a **weight** (`w1, w2, ...`).
  3. Adding a **bias (b)**.
  4. Passing the result through an **activation function** (e.g., sigmoid).

👉 Formula:

```
z = w1*x1 + w2*x2 + ... + b  
a = activation(z)
```

* `z` = weighted sum + bias
* `a` = neuron’s output

---

## 2. 🏗️ Layers in a Neural Network

* **Input Layer** 🎯 → first layer, takes in raw data (numbers, images, text).
* **Hidden Layers** 🧩 → middle layers where learning happens. Can be **1 or many**.
* **Output Layer** 📊 → gives the final prediction (classification, number, text, etc.).

---

## 3. ⚡ Forward Propagation (How Data Flows)

* Forward propagation = **data moves from input → hidden layers → output**.
* At each neuron:

  1. Compute **weighted sum + bias**.
  2. Apply **activation function**.
  3. Pass output to the next layer.

---

## 4. 🎛️ Activation Functions

Why do we need them?

* Without them → network is just **linear regression**.
* With them → network can learn **non-linear, complex tasks** (like image recognition, translation).

Popular one:

* **Sigmoid function**

  * If `z` → large positive → output close to **1**.
  * If `z` → large negative → output close to **0**.

👉 Decides whether a neuron should "fire" (activate) or not.

---

## 5. 🧮 Example: Single Neuron

* Input: `x1 = 0.1`
* Weight: `w1 = 0.15`
* Bias: `b1 = 0.4`

Step 1: Compute `z`

```
z = w1*x1 + b1  
z = (0.15 * 0.1) + 0.4  
z = 0.415
```

Step 2: Apply sigmoid

```
a = sigmoid(z) ≈ 0.6023
```

✅ Output = **0.6023**

---

## 6. 🔗 Example: 2 Neurons (Chained)

* Neuron 1 output (`a1`) → becomes input for Neuron 2.
* Neuron 2 computes:

```
z2 = w2*a1 + b2  
a2 = sigmoid(z2) ≈ 0.7153
```

👉 Final prediction = **0.7153**

---

## 7. 📌 Key Takeaways

* ANN = many **perceptrons** stacked in **layers**.
* **Input → Hidden → Output**.
* **Forward propagation**: input flows forward through the network, producing an output.
* **Activation functions** make ANNs powerful by allowing **non-linear transformations**.
* Given **weights and biases**, you can compute the **output for any input**.

---

✅ **Quick Pro Explanation for Beginners:**
Think of a neural network like a **factory**:

* Input layer = raw materials 🚚
* Hidden layers = machines that refine & transform 🏭
* Output layer = final product 📦
* Activation functions = decision switches 🔘 that let the machines make **complex transformations**, not just simple ones.

---

👉 Do you want me to also create a **colorful side-by-side Markdown table** comparing **Forward Propagation vs Backpropagation**, so you’ll be ready when the course moves to the next topic?
