# Transformers for Classification (Encoder)

---

### 🔑 Why use Transformers?

* Traditional neural networks (like simple feed-forward or RNNs) can **lose context**.
* Transformers with **attention layers** process **all words together**, keeping relationships between words.
* Example:

  * *"The bank of the river"* vs *"The bank gave a loan"* → Transformers know "bank" means different things depending on context.

---

### 🛠️ Pipeline Setup

1. **Dataset** → Example: AG\_NEWS (news articles + category labels).
2. **Split** → Training (95%), Validation (5%), and Test.
3. **Tokenizer** → Break sentences into tokens (words → numbers).
4. **Vocabulary** → Map tokens to integer IDs.
5. **Padding** → Add `0`s to shorter sequences so all batches have the same length.
6. **DataLoader** → Groups samples into batches for training.

---

### 🧩 Transformer Encoder Model

1. **Embedding Layer**

   * Converts token IDs into vectors (e.g., size = 100).
   * Example: `"football"` → `[0.2, -0.1, 0.5, …]`.

2. **Positional Encoding (PE)**

   * Adds order info (because Transformers read words in parallel).
   * Without PE → "I like football" = "Football like I".

3. **Transformer Encoder Layers**

   * Stacks of self-attention + feedforward.
   * Capture relationships between words.
   * Output = **contextual embeddings** (each word embedding now includes its context).

4. **Pooling (Mean over tokens)**

   * Average embeddings across sequence → one vector per text.
   * Example: 64 samples → 64 vectors (each 100-dim).

5. **Linear Classifier**

   * Input: context vector (100 features).
   * Output: prediction of class (e.g., Business, Sports, Tech, etc).

---

### 📈 Training

* **Loss Function**: CrossEntropy (good for multi-class).
* **Optimizer**: SGD (learning rate = 0.1).
* **Scheduler**: Reduces learning rate by 0.1 after each epoch.
* **Epochs**: Loop over dataset multiple times.
* **Trend**: As **loss ↓**, **accuracy ↑**.

---

### 📝 Key Intuition

* Transformer encoder works like a **super-reader**:

  * It reads the whole text at once.
  * It understands both the **meaning of words** and **their positions**.
  * It then summarizes everything into a single vector → **classifier predicts the label**.

---

✅ **Recap (for dummies):**

1. Prepare data → tokenize, pad, batch.
2. Build model → Embedding → Positional Encoding → Transformer Encoder → Pool → Classifier.
3. Train → CrossEntropy + SGD → track loss & accuracy.
4. Transformers keep context, so they classify text more accurately than old models.

---

Would you like me to also create a **step-by-step flowchart (visual)** for this pipeline so you can glance and remember the whole process?
