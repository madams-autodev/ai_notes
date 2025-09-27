# Activation Functions in Neural Networks

## 1. Why Do We Need Activation Functions?
- Neural networks combine inputs with weights & biases → but without activation functions, it’s just **linear math**.
- Activation functions make the network **non-linear**, which allows:
  - Detecting complex patterns (images, text, voice, etc.)
  - Enabling deep learning.

Think of them as **"decision gates"** that decide whether a neuron should "fire" or not.

---

## 2. 🧮 Common Activation Functions

### 2.1 🌀 Sigmoid
Formula:  
\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

- Outputs between **0 and 1**.
- Example:  
  - If input = 0 → output = 0.5  
  - If input = 10 → output ≈ 1  
  - If input = -10 → output ≈ 0  

✅ Good for probabilities.  
❌ **Problems**:
- **Vanishing Gradient**: For very high or low inputs, slope ≈ 0 → network stops learning.  
- Outputs only positive (0–1), not centered around 0.

---

### 2.2 📈 Hyperbolic Tangent (tanh)
Formula:  
\[
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
\]

- Outputs between **-1 and +1**.  
- Symmetric around 0 → fixes the "always positive" issue of Sigmoid.  

✅ Centered at 0 → better than sigmoid.  
❌ Still suffers from **vanishing gradient** in deep networks.  

---

### 2.3 🔲 ReLU (Rectified Linear Unit)
Formula:  
\[
f(z) = \max(0, z)
\]

- If input < 0 → output = 0  
- If input ≥ 0 → output = input  

✅ Advantages:
- Simple & fast.  
- Helps avoid vanishing gradient.  
- Sparse activation: only some neurons fire → efficient.  

❌ Problem: "Dead ReLU" → some neurons may **always output 0** if they only get negative inputs.

---

### 2.4 ⚡ Leaky ReLU
Formula:  
\[
f(z) = \begin{cases} 
z & \text{if } z > 0 \\ 
0.01z & \text{if } z \leq 0 
\end{cases}
\]

- Fix for "Dead ReLU" → gives small slope for negative values.  

---

### 2.5 📊 Softmax
Formula:  
\[
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}
\]

- Converts numbers → **probability distribution**.  
- Example: raw output = `[1.6, 0.55, 0.98]`  
  - After softmax = `[0.51, 0.18, 0.31]`  

✅ Used in **output layer for classification** (pick the class with highest probability).  

---

## 3. 🚀 Which Functions Are Used Today?
- **Sigmoid**: Rarely used (hidden layers), only for probabilities.  
- **Tanh**: Better than sigmoid, but still causes vanishing gradient.  
- **ReLU**: 🔥 Most popular for hidden layers.  
- **Leaky ReLU**: Used when ReLU has “dead neurons”.  
- **Softmax**: Used in output layer for **multi-class classification**.  

---

## 4. 🎯 Quick Summary
- Sigmoid → [0,1], probability but causes vanishing gradients.  
- Tanh → [-1,1], symmetric but still vanishes in deep nets.  
- ReLU → most common, fast, avoids vanishing gradient.  
- Leaky ReLU → fix for dead ReLUs.  
- Softmax → used in final layer for classification → outputs probabilities.

---

💡 **Analogy**:
- Sigmoid = dimmer switch (values squeezed between 0–1).  
- Tanh = balanced dimmer (can be negative or positive).  
- ReLU = light switch (off = 0, on = brightness level).  
- Softmax = voting system (turns outputs into % probabilities).
```

---

👉 Do you want me to also **draw simple plots** (Sigmoid curve, ReLU shape, Softmax distribution) so you can visualize each function’s behavior?
