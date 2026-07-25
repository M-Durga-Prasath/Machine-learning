
# Question 1: Explain the complete pipeline from raw text to retrieval.

## Mine

Tokenization is the process wherein we split the incoming or input text into smaller parts known as tokens. For example, if we receive a sentence as an input, then each word will be considered as a token. And we make sure, we need this because to understand the context, we as humans can read the whole sentence and understand the context, but computers cannot. So we need individual tokens. Also for various analysis such as semantic analysis, syntactic analysis, the grammar check, how each word plays into the, each word is important, all that is needed. The output looks like each word of a sentence. For example, let's say the example is, Rahul is a good boy. He is playing outside. Then Rahul, is, a, good, boy, he, is, these are all tokens. And for a specialized word such as playing, it is split into two, like play and ing, because when new words come into play, they are made up of the older words. So the system does not need to memorize new words. It can just combine the older words and understand the context by itself.

## Proper

Tokenization is the process of splitting the input text into smaller units called tokens. (Instead of saying "each word becomes a token," say "the text is split into tokens," because modern tokenizers often split words into subwords rather than treating every word as a single token.)

For example, if the input sentence is:

"I love machine learning."

The tokenizer may produce:

["I", "love", "machine", "learning"]

or for a word like "playing", it may produce:

["play", "ing"]

This is because modern language models use subword tokenization, which helps them handle new or rare words by combining smaller known pieces instead of memorizing every possible word.

We need tokenization because computers cannot process raw text directly—they only understand numbers. (Instead of saying "we need individual tokens to understand the context," explain that tokenization is the first preprocessing step that prepares text for the model.)

After tokenization, each token is converted into a unique token ID, such as:

["I", "love", "AI"]

↓

[102, 209, 4812]

These token IDs are then passed to the embedding layer, where they are converted into dense vectors that the transformer can process.

Instead of saying tokenization is mainly for semantic analysis, syntactic analysis, or grammar checking, mention that its primary role in transformers is to convert text into a format that can eventually be represented as numbers and processed by the model.

---

# Question 2: What is the embedding layer?

## Mine

An embedding layer is a layer which converts tokens into specific vector for in a vector format, in a format which the computer can understand. Usually, neural networks deal with numbers instead of the words directly. So, it converts each word into a set of, like, vectors. Each vector is formed by asking a question, such as, for example, if I say king, a word king, then I ask another question, is it a human? Then the range is between some numbers. So, it, let's say, 0.6 for it being a person. For it being a person. Now, followed by, I will ask whether can it fly. A king can't obviously fly, so it will be some other numbers. Similarly, we ask some other questions for it, and based on that, we get what it is. Also, the output, it looks like how many questions are asked to the word token, token entity, token. So, how many questions is usually depending on the different models. BERT asks 384 questions, like, not questions. The size of the embedding depends on the questions. So, usually the size is 384 for the BERT, 784 for other models. Some also models use more than that. It depends. It helps us determine how the token is converted into numbers.

## Proper

1. "It converts each word into vectors."

❌ Not exactly.

Remember:

The embedding layer converts token IDs, not words, into vectors.

Pipeline:

Sentence
↓
Tokenizer
↓
Tokens
↓
Token IDs
↓
Embedding Layer
↓
Embedding Vectors

So don't skip the token ID step.

2. "Each vector is formed by asking questions."

the biggest mistake.

This is a common way to build intuition, but it is not how embeddings are actually created.

The model is not asking predefined questions like:

Is it a human?
Can it fly?

Instead:

The embedding layer is simply a large lookup table (embedding matrix).

Example:

Token ID 102
↓

[0.21, -0.54, 1.18, ...]

These values are learned automatically during training, not assigned by answering human-readable questions.

You can think of each dimension as representing some learned feature, but we usually don't know what each individual dimension means.

3. "384 questions... BERT asks 384 questions."

The model is not asking 384 questions.

Instead:

384 is the embedding dimension (vector size), not the number of questions.

For example:

Token ID

↓

[0.25, -0.81, 0.44, ..., 384 values]

Each value is one dimension of the embedding vector.

4. "784 for other models."

❌ Incorrect number.

Common embedding sizes include:

MiniLM → 384
BERT Base → 768
BERT Large → 1024

784 is not a standard embedding dimension.

5. "It helps us determine how the token is converted into numbers."

Better:

It converts each token ID into a dense numerical representation that captures semantic meaning and can be processed by the transformer.

Polished Version 

An embedding layer is a layer that converts token IDs into dense vectors that neural networks can process. (Instead of saying it converts words directly, remember that the tokenizer first converts text into token IDs, and the embedding layer works on those IDs.)

For example:

Sentence

↓

Tokens

↓

Token IDs

↓

Embedding Layer

↓

Embedding Vectors

If a token ID is:

102

the embedding layer might convert it into:

[0.24, -0.83, 1.12, ..., 384 values]

These values are not created by asking predefined questions like "Is it a human?" or "Can it fly?". Instead, the embedding layer is a learned lookup table (embedding matrix), where each token ID is mapped to a vector whose values are learned automatically during training.

The size of this vector is called the embedding dimension, not the number of questions. Different models use different embedding sizes. For example, MiniLM commonly uses 384 dimensions, while BERT Base uses 768 dimensions.

These embedding vectors capture semantic information, so words with similar meanings tend to have similar vector representations. These vectors are then passed to the transformer layers for further contextual processing.


==========================================================
The embedding layer converts token IDs into dense numerical vectors that the transformer can understand. Since neural networks work with numbers rather than text, each token ID is mapped to a learned vector from an embedding matrix. These vectors are not manually designed or based on predefined questions; instead, their values are learned automatically during model training. The length of each vector is called the embedding dimension, which varies across models—for example, 384 or 768 dimensions. These embeddings capture semantic information and serve as the input to the transformer, where they are further refined using self-attention.
==========================================================

---

# Question 3: What is positional encoding?

## Mine

Positional encoding is a process wherein we assign which position does each token is present in. It is usually done with the embedding matrix to tell what are the positions so that we can keep the syntactic information for the machine to understand which position, which word is at which position. If we did not use it, then the positions can be jumbled up, due to which the meaning of the words, meaning of the sentence can be ambiguous or it is interpreted differently. You usually add a position matrix with the embedding matrix and convert it into another matrix, which contains both the positional embeddings and the normal embeddings. Yes.

## Proper

1. "We assign which position each token is present in."

A better way to say it is:

Positional encoding encodes the position of each token into a vector so the transformer knows the order of the tokens.

The position itself isn't just a number like 1, 2, 3—it is represented as a position vector.

2. "It is usually done with the embedding matrix."

It isn't "done with the embedding matrix."

A clearer explanation is:

A positional encoding vector is generated for each position and added to the token embedding vector.

3. "You add a position matrix with the embedding matrix."

Technically, we don't usually describe it as adding two matrices.

We say:

Each token embedding is added element-wise to its corresponding positional encoding vector.

For example:

Token Embedding

+

Position Encoding

=

Input Embedding

4. Missing one important point

didn't mention why transformers specifically need positional encoding.

Unlike RNNs, transformers process all tokens in parallel, so they don't naturally know which token comes first or last. Positional encoding provides this order information.


Polished Version

Positional encoding is a technique used to provide information about the order of tokens in a sentence. (Instead of saying we simply assign positions, say that each position is represented by a positional encoding vector that captures the token's location in the sequence.)

Transformers process all tokens in parallel, so they do not naturally know which token comes first, second, or last. Positional encoding solves this problem by giving every token information about its position.

For example:

I love machine learning

↓

I → Position 1

love → Position 2

machine → Position 3

learning → Position 4

A positional encoding vector is generated for each position and is added to the corresponding token embedding vector. (Instead of saying a position matrix is added to the embedding matrix, explain that each token embedding is combined with its positional encoding vector.)

The resulting vectors now contain both the semantic meaning of the token and its position in the sentence.

Without positional encoding, the transformer would treat the sentence as an unordered collection of tokens, making it difficult to distinguish between sentences like:

Dog bites man
Man bites dog

Even though they contain the same words, the meanings are completely different because of their order.

==================================================

Positional encoding is a technique that gives the transformer information about the order of tokens in a sentence. Since transformers process all tokens in parallel, they don't naturally know which word comes first or last. To solve this, a positional encoding vector is generated for each token position and added to its embedding vector. The resulting input embeddings contain both the semantic meaning of the token and its position in the sequence. Without positional encoding, the transformer would lose word-order information and could misinterpret sentences that contain the same words in different orders.

==================================================
---

# Question 4: What is self-attention?

## Mine

Self-attention is a process wherein we tell how much attention does each word get inside a sentence. Usually, not every word is meant to get equal attention. So some words usually get more attention than others so that we can build the context around it. The tokens which, each token has an embedding matrix. So it interacts with other tokens telling how far apart it is so that it can tell what the context is. I mean, yes. For example, if I say Apple released an iPhone, also Apple released a phone. So the word Apple will resemble most with the word phone, telling it is a company building the context around it. And if I say, I ate an apple, it will be the word that will be most resembling to the word apple, telling it is a fruit. So that's how the self-attention process works.

## Proper

Self-attention is a mechanism that allows each token to look at every other token in the sentence and determine how important they are for understanding its meaning. (Instead of saying "we tell how much attention each word gets," remember that the model learns these attention weights automatically during training.)

Not every surrounding word is equally important. Some words contribute more to the meaning of a token than others, so the model assigns them higher attention weights.

Each token starts with an embedding vector, not an embedding matrix. During self-attention, every token compares its embedding with the embeddings of all other tokens to determine which ones are most relevant for understanding the context. (Instead of saying it checks how far apart words are, remember that self-attention measures semantic relevance, not physical distance in the sentence.)

For example:

Apple released a new phone.

Here, the token Apple attends strongly to words like released and phone, helping the model understand that Apple refers to the company.

In another sentence:

I ate an apple.

The word apple attends strongly to ate, helping the model understand that it refers to the fruit.

After self-attention, every token receives a new contextual embedding, meaning its representation has been updated using information from the entire sentence.

==============================================
Self-attention is a mechanism that allows each token in a sentence to interact with every other token and determine which ones are most important for understanding its meaning. Instead of treating every surrounding word equally, the model learns attention weights that indicate the relevance of each token in the current context. This enables the same word to have different meanings in different sentences. For example, in "Apple released a new phone," the word "Apple" attends to words like "released" and "phone," indicating the company. In "I ate an apple," it attends to "ate," indicating the fruit. The output of self-attention is a contextual embedding for each token that captures its meaning within the sentence.
==============================================
---


# Question 9: What are contextual token embeddings?

## Mine

<!-- Write your explanation here -->

## Proper

<!-- Fill this after review -->

---

# Question 10: What is pooling ?

## Mine

Pooling is the process wherein each word can, if assigned a different embedding matrix, then it will lead to a large amount of data. For each word we say, for example, for the BERT model, there is 768, the dimension of embedding matrix is 768. For each word, it will be 768. So it would lead to a large amount of data. So what we do is, we pool all of them together into a single word. Say BERT is a CLS and SCP, wherein for seeing what this sentence means, then we look up at CLS and we will get what this sentence is trying to select. We get the details about the embedding matrix of this sentence.

## Proper

1. "Each word is assigned a different embedding matrix."


Each word/token gets an embedding vector, not an embedding matrix.

Remember:

Embedding Matrix → One large lookup table for the whole vocabulary.
Embedding Vector → One row selected from that matrix for a specific token.

2. "Pooling is done because otherwise there is too much data."


The primary reason is:

Many downstream tasks (semantic search, retrieval, clustering, classification) require one fixed-length vector for the entire sentence, not one vector per token.

Reducing the amount of data is a side effect, not the main purpose.

3. "We pool all of them together into a single word."


We do not convert them into a single word.

We convert them into one sentence embedding (one vector representing the whole sentence).

Pooling is the process of combining the contextual embeddings of all tokens into one fixed-length sentence embedding. (Instead of saying each word has an embedding matrix, remember that each token has an embedding vector.)

After the transformer processes the sentence, every token has its own contextual embedding.

For example:

I          → 768-dimensional vector

love       → 768-dimensional vector

machine    → 768-dimensional vector

learning   → 768-dimensional vector

Many NLP tasks, such as semantic search and retrieval, require one vector for the entire sentence, not one vector for every token. (Instead of saying pooling is mainly done to reduce data size, explain that it creates a single representation of the whole sentence.)

There are several common pooling methods:

Mean Pooling – Take the average of all token embeddings.
Max Pooling – Take the maximum value from each dimension across all token embeddings.
CLS Pooling – Use the final contextual embedding of the [CLS] token as the sentence representation. (Instead of saying "CLS and SCP," the correct terms are "CLS" and "SEP," and SEP is not used for pooling.)

The output of pooling is one sentence embedding, which can then be compared with other sentence embeddings using cosine similarity.

===========================================
After the transformer processes a sentence, it produces one contextual embedding for each token. However, many downstream tasks such as semantic search and retrieval require a single fixed-length vector representing the entire sentence. Pooling solves this by combining all token embeddings into one sentence embedding. Common pooling methods include mean pooling, max pooling, and CLS pooling, where the final embedding of the CLS token is used as the sentence representation. This sentence embedding can then be compared with other sentence embeddings using similarity measures like cosine similarity.
===========================================

---

# Question 6: What are Cosine Similarity and Retrieval?

## Mine

Cosine similarity is the process of calculating how much the words are similar to each other. Usually, the words that are similar to each other point towards the same direction, while the words that are not similar to each other point in the opposite direction. If words are similar to each other, they will be close to one. If not, they will be close to zero. Also, the words are usually calculated using the sentence embedding. First, the words are converted into token IDs, which are then converted into sentence embeddings. These sentence embeddings are then put into the cosine similarity formula, and the similarity is retrieved. For the retrieval, and also, if the words are not similar to each other, it will be minus one, as one, zero. The retrieval works such as follows. First, the words, the query is embedded. The query is then compared to the chunk embeddings of the docs, and the most relevant ones, which are calculated using cosine similarity, are retrieved. And based on this chunk, we set the context of the query, which is then given to the LLM for the data augmentation process.

## Proper


3. Cosine similarity scores

🟡 Small clarification.

You said:

Similar → 1

Not similar → 0

Minus one

A more precise explanation is:

1 → Same direction (very similar)
0 → Orthogonal (unrelated)
-1 → Opposite direction (rare in embedding models and usually not seen much in practice)

Interviewers like this distinction.

4. "Data augmentation process."

❌ Incorrect terminology.

This is probably the only major terminology mistake.

It is:

Retrieval-Augmented Generation (RAG)

or

The retrieved chunks are augmented to the prompt/context before being sent to the LLM.

Data augmentation is a completely different ML concept (creating more training data by modifying existing data).



======================================

Cosine similarity is a metric that measures how similar two embedding vectors are by comparing the angle between them. In a RAG system, the user's query is first converted into a sentence embedding. This embedding is then compared with the stored document or chunk embeddings using cosine similarity. A score close to 1 indicates high semantic similarity, a score close to 0 indicates little or no relation, and a score close to -1 indicates opposite directions, although this is uncommon in practice. The top-k most similar chunks are retrieved and added to the prompt as context. The LLM then uses this retrieved context to generate a more accurate and relevant answer.
======================================

---


=======================================Recuring problems===============================================================

❌ Embedding matrix vs. embedding vector
❌ Words vs. token IDs
❌ Words vs. embeddings
❌ Data augmentation vs. Retrieval-Augmented Generation (RAG)

=====================================================================================================================