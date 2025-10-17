"""
Improved Activity 2 Solution - Achieve >90% Accuracy
Uses advanced feature engineering and optimized models
"""

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

print("="*70)
print("IMPROVED ACTIVITY 2 - Advanced Feature Engineering")
print("="*70)

# Load data
df = pd.read_csv('data/dga-24000.csv')
print(f"\nDataset: {df.shape}")
print(f"Classes: {df['Family'].nunique()}")

# Extract domain without TLD
df['domain_name'] = df['Domain'].str.split('.').str[0]

def extract_advanced_features(domain):
    """Extract comprehensive features for better classification"""
    domain_lower = domain.lower()
    length = len(domain)

    if length == 0:
        return {f'feature_{i}': 0 for i in range(25)}

    # Basic counts
    alpha_count = sum(c.isalpha() for c in domain)
    digit_count = sum(c.isdigit() for c in domain)
    special_count = sum(not c.isalnum() for c in domain)

    vowels = 'aeiou'
    vowel_count = sum(c in vowels for c in domain_lower)
    consonant_count = alpha_count - vowel_count

    # Ratios
    alpha_ratio = alpha_count / length
    digit_ratio = digit_count / length
    vowel_ratio = vowel_count / length
    consonant_ratio = consonant_count / length

    # Entropy
    char_freq = Counter(domain_lower)
    entropy = -sum((count/length) * np.log2(count/length)
                   for count in char_freq.values() if count > 0)

    # Consecutive chars
    import itertools
    max_consecutive = max((sum(1 for _ in group)
                          for char, group in itertools.groupby(domain_lower)),
                          default=0)

    # Unique ratios
    unique_chars = len(set(domain_lower))
    unique_ratio = unique_chars / length

    # N-gram diversity
    bigrams = [domain_lower[i:i+2] for i in range(len(domain_lower)-1)]
    trigrams = [domain_lower[i:i+3] for i in range(len(domain_lower)-2)]

    bigram_diversity = len(set(bigrams)) / len(bigrams) if bigrams else 0
    trigram_diversity = len(set(trigrams)) / len(trigrams) if trigrams else 0

    # Pronounceability - consecutive consonants
    consonant_chunks = []
    current_chunk = 0
    for c in domain_lower:
        if c.isalpha() and c not in vowels:
            current_chunk += 1
        else:
            if current_chunk > 0:
                consonant_chunks.append(current_chunk)
            current_chunk = 0
    if current_chunk > 0:
        consonant_chunks.append(current_chunk)

    max_consonant_chunk = max(consonant_chunks) if consonant_chunks else 0
    avg_consonant_chunk = np.mean(consonant_chunks) if consonant_chunks else 0

    # Digit patterns
    has_digit = int(digit_count > 0)
    starts_digit = int(domain[0].isdigit()) if domain else 0
    ends_digit = int(domain[-1].isdigit()) if domain else 0

    # Special patterns
    has_hyphen = int('-' in domain)
    num_dots = domain.count('.')

    return {
        'length': length,
        'alpha_count': alpha_count,
        'digit_count': digit_count,
        'special_count': special_count,
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        'alpha_ratio': alpha_ratio,
        'digit_ratio': digit_ratio,
        'vowel_ratio': vowel_ratio,
        'consonant_ratio': consonant_ratio,
        'entropy': entropy,
        'max_consecutive': max_consecutive,
        'unique_chars': unique_chars,
        'unique_ratio': unique_ratio,
        'bigram_diversity': bigram_diversity,
        'trigram_diversity': trigram_diversity,
        'max_consonant_chunk': max_consonant_chunk,
        'avg_consonant_chunk': avg_consonant_chunk,
        'has_digit': has_digit,
        'starts_digit': starts_digit,
        'ends_digit': ends_digit,
        'has_hyphen': has_hyphen,
        'num_dots': num_dots,
        'length_squared': length ** 2,
        'entropy_length_ratio': entropy / length if length > 0 else 0
    }

print("\nExtracting advanced features...")
features_list = [extract_advanced_features(d) for d in df['domain_name']]
features_df = pd.DataFrame(features_list)

print(f"Statistical features: {features_df.shape}")

# N-gram features with higher max_features
print("\nExtracting n-gram features...")
vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(2, 5),  # Increased to 5-grams
    max_features=1000,    # More features
    lowercase=True,
    min_df=2
)

ngram_features = vectorizer.fit_transform(df['domain_name']).toarray()
print(f"N-gram features: {ngram_features.shape}")

# Combine features
X_combined = np.hstack([features_df.values, ngram_features])
print(f"Combined features: {X_combined.shape}")

# Prepare labels
y = df['Family'].values
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_combined)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
)

print(f"\nTraining set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

# Train multiple models
print("\n" + "="*70)
print("MODEL TRAINING")
print("="*70)

results = {}

# Logistic Regression with increased iterations
print("\n1. Logistic Regression...")
lr = LogisticRegression(max_iter=2000, random_state=42, n_jobs=-1, C=10)
lr.fit(X_train, y_train)
lr_acc = accuracy_score(y_test, lr.predict(X_test))
results['Logistic Regression'] = lr_acc * 100
print(f"   Accuracy: {lr_acc*100:.2f}%")

# Random Forest with more trees
print("\n2. Random Forest...")
rf = RandomForestClassifier(n_estimators=200, max_depth=None,
                            random_state=42, n_jobs=-1, min_samples_split=2)
rf.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf.predict(X_test))
results['Random Forest'] = rf_acc * 100
print(f"   Accuracy: {rf_acc*100:.2f}%")

# MLP with larger architecture
print("\n3. MLP Neural Network...")
mlp = MLPClassifier(hidden_layer_sizes=(200, 100, 50), max_iter=500,
                    random_state=42, early_stopping=True,
                    validation_fraction=0.1, n_iter_no_change=20)
mlp.fit(X_train, y_train)
mlp_acc = accuracy_score(y_test, mlp.predict(X_test))
results['MLP'] = mlp_acc * 100
print(f"   Accuracy: {mlp_acc*100:.2f}%")

# Gradient Boosting
print("\n4. Gradient Boosting...")
gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1,
                                random_state=42, max_depth=5)
gb.fit(X_train, y_train)
gb_acc = accuracy_score(y_test, gb.predict(X_test))
results['Gradient Boosting'] = gb_acc * 100
print(f"   Accuracy: {gb_acc*100:.2f}%")

# Results summary
print("\n" + "="*70)
print("FINAL RESULTS")
print("="*70)

for model_name, acc in sorted(results.items(), key=lambda x: x[1], reverse=True):
    status = "PASS >90%" if acc >= 90 else "FAIL <90%"
    print(f"{model_name:25s}: {acc:6.2f}%  [{status}]")

best_model = max(results, key=results.get)
best_acc = results[best_model]

print("\n" + "="*70)
print(f"BEST MODEL: {best_model}")
print(f"ACCURACY: {best_acc:.2f}%")

if best_acc >= 90:
    print("\nSUCCESS: Requirement of >90% accuracy achieved!")
else:
    print(f"\nSTILL SHORT: Need {90-best_acc:.2f}% more")
    print("Consider: More data preprocessing, feature selection, or ensemble methods")

print("="*70)
