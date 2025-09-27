# What is Regression?
- Regression = predicting a number (continuous value) instead of a category.  
Example:
- Classification → Is this email spam or not? (Yes/No).  
- Regression → What will the price of this house be? (a number).  



# Example Dataset: Concrete Strength
Each row = one sample of concrete mix.  
**Features (X, inputs):**
- Cement  
- Blast furnace slag  
- Fly ash  
- Water  
- Superplasticizer  
- Coarse aggregate  
- Fine aggregate  
- Age (days)

**Target (y, output):**
- Compressive strength (a number)

👉 Example row:  
`[540, 0, 0, 162, 2.5, 1040, 676, 28] → 79.99 MPa`

---

## 3. Neural Network Structure
We build a **Dense (fully connected) network**:

- Input layer → 8 features  
- Hidden layer 1 → 5 neurons (ReLU)  
- Hidden layer 2 → 5 neurons (ReLU)  
- Output layer → 1 neuron (linear, since regression gives numbers)  

🔗 Every node in one layer is connected to **all nodes in the next layer** (dense network).

---

## 4. Preparing Data
We split data into:
- **Predictors (X):** all 8 features  
- **Target (y):** compressive strength  

```python
X = concrete_data.drop(columns=['Strength'])
y = concrete_data['Strength']
````

---

## 5. Building the Model with Keras

We use **Sequential API** (easy for linear stacks of layers).

```python
from keras.models import Sequential
from keras.layers import Dense

# 1. Define the model
model = Sequential()

# 2. Add hidden layers
model.add(Dense(5, activation='relu', input_shape=(8,)))  # 8 inputs
model.add(Dense(5, activation='relu'))

# 3. Add output layer
model.add(Dense(1))  # single output for regression
```

---

## 6. Compile the Model

We need:

* **Loss function** → how wrong the model is

  * For regression: **Mean Squared Error (MSE)**
  * Formula:

    $$
    MSE = \frac{1}{n} \sum (y_{true} - y_{pred})^2
    $$
* **Optimizer** → how to update weights

  * We use **Adam** (faster than vanilla gradient descent).

```python
model.compile(optimizer='adam', loss='mean_squared_error')
```

---

## 7. Train the Model

We fit the model on our dataset.

```python
model.fit(X, y, epochs=50, verbose=1)
```

* `epochs=50` → how many times the model sees the whole dataset.
* `verbose=1` → shows progress bar during training.

---

## 8. Make Predictions

Once trained, we can predict new samples.

```python
predictions = model.predict(X[:5])
print(predictions)
```

Example output:

```
[[80.2]
 [45.7]
 [67.4]
 [89.1]
 [32.5]]
```

---

## 9. Key Takeaways

* **Regression = predicting numbers**.
* We split data into **features (X)** and **target (y)**.
* Keras makes it easy to build networks with **Sequential + Dense layers**.
* **ReLU** → hidden layers; **Linear output** → regression.
* Use **Adam optimizer + MSE loss** for regression problems.

💡 You can build a regression model in **<10 lines of code** with Keras!

```

---

```

Keras Activation Functions: https://keras.io/activations/
Keras Models: https://keras.io/models/about-keras-models/#about-keras-models
Keras Optimizers: https://keras.io/optimizers/
Keras Metrics: https://keras.io/metrics/