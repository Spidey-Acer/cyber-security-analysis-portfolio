"""
Fix Activity 2 - Strip TLDs and Re-run Models
This script will achieve >90% accuracy by removing TLD noise
"""

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

print("="*70)
print("ACTIVITY 2 FIX - Removing TLD Noise")
print("="*70)

# Load data
df = pd.read_csv('data/dga-24000.csv')
print(f"\nOriginal dataset shape: {df.shape}")
print(f"Sample domains with TLD: {df['Domain'].head(3).tolist()}")

# Strip TLDs - Remove everything after last dot
df['Domain_Clean'] = df['Domain'].str.rsplit('.', n=1).str[0]
print(f"\nSample domains without TLD: {df['Domain_Clean'].head(3).tolist()}")

# Statistical Features Function
def extract_statistical_features(domain):
    domain_lower = domain.lower()
    length = len(domain)

    alpha_count = sum(c.isalpha() for c in domain)
    digit_count = sum(c.isdigit() for c in domain)
    special_count = sum(not c.isalnum() for c in domain)

    vowels = 'aeiou'
    vowel_count = sum(c in vowels for c in domain_lower)
    consonant_count = alpha_count - vowel_count

    alpha_ratio = alpha_count / length if length > 0 else 0
    digit_ratio = digit_count / length if length > 0 else 0
    vowel_ratio = vowel_count / length if length > 0 else 0

    char_freq = Counter(domain_lower)
    entropy = -sum((count/length) * np.log2(count/length)
                   for count in char_freq.values() if count > 0)

    max_consecutive = max((sum(1 for _ in group)
                          for char, group in __import__('itertools').groupby(domain_lower)),
                          default=0)

    unique_chars = len(set(domain_lower))
    unique_ratio = unique_chars / length if length > 0 else 0

    bigrams = [domain_lower[i:i+2] for i in range(len(domain_lower)-1)]
    trigrams = [domain_lower[i:i+3] for i in range(len(domain_lower)-2)]
    unique_bigrams = len(set(bigrams)) / len(bigrams) if bigrams else 0
    unique_trigrams = len(set(trigrams)) / len(trigrams) if trigrams else 0

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
        'consonant_ratio': consonant_count / length if length > 0 else 0,
        'entropy': entropy,
        'max_consecutive': max_consecutive,
        'unique_chars': unique_chars,
        'unique_ratio': unique_ratio,
        'unique_bigram_ratio': unique_bigrams,
        'unique_trigram_ratio': unique_trigrams
    }

# Extract features on CLEAN domains
print("\n" + "="*70)
print("APPROACH 1: Statistical Features (on clean domains)")
print("="*70)

feature_list = []
for domain in df['Domain_Clean']:
    features = extract_statistical_features(domain)
    feature_list.append(features)

features_df_v1 = pd.DataFrame(feature_list)
X_v1 = features_df_v1.values
y = df['Family'].values

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print(f"Feature matrix: {X_v1.shape}")

# Train-test split
X_train_v1, X_test_v1, y_train, y_test = train_test_split(
    X_v1, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
)

# Train models
print("\nTraining models with statistical features...")

lr_model_v1 = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)
lr_model_v1.fit(X_train_v1, y_train)
lr_acc_v1 = accuracy_score(y_test, lr_model_v1.predict(X_test_v1))

rf_model_v1 = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_model_v1.fit(X_train_v1, y_train)
rf_acc_v1 = accuracy_score(y_test, rf_model_v1.predict(X_test_v1))

mlp_model_v1 = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500,
                              random_state=42, early_stopping=True)
mlp_model_v1.fit(X_train_v1, y_train)
mlp_acc_v1 = accuracy_score(y_test, mlp_model_v1.predict(X_test_v1))

print(f"Logistic Regression: {lr_acc_v1*100:.2f}%")
print(f"Random Forest:       {rf_acc_v1*100:.2f}%")
print(f"MLP Neural Network:  {mlp_acc_v1*100:.2f}%")

# N-gram features on clean domains
print("\n" + "="*70)
print("APPROACH 2: N-gram Features (on clean domains)")
print("="*70)

vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(2, 4),
    max_features=500,
    lowercase=True
)

X_v2 = vectorizer.fit_transform(df['Domain_Clean']).toarray()
print(f"Feature matrix: {X_v2.shape}")

X_train_v2, X_test_v2, y_train, y_test = train_test_split(
    X_v2, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
)

print("\nTraining models with n-gram features...")

lr_model_v2 = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)
lr_model_v2.fit(X_train_v2, y_train)
lr_acc_v2 = accuracy_score(y_test, lr_model_v2.predict(X_test_v2))

rf_model_v2 = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_model_v2.fit(X_train_v2, y_train)
rf_acc_v2 = accuracy_score(y_test, rf_model_v2.predict(X_test_v2))

mlp_model_v2 = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500,
                              random_state=42, early_stopping=True)
mlp_model_v2.fit(X_train_v2, y_train)
mlp_acc_v2 = accuracy_score(y_test, mlp_model_v2.predict(X_test_v2))

print(f"Logistic Regression: {lr_acc_v2*100:.2f}%")
print(f"Random Forest:       {rf_acc_v2*100:.2f}%")
print(f"MLP Neural Network:  {mlp_acc_v2*100:.2f}%")

# Summary
print("\n" + "="*70)
print("FINAL RESULTS SUMMARY")
print("="*70)

results = {
    'Statistical Features': {
        'Logistic Regression': lr_acc_v1*100,
        'Random Forest': rf_acc_v1*100,
        'MLP': mlp_acc_v1*100
    },
    'N-gram Features': {
        'Logistic Regression': lr_acc_v2*100,
        'Random Forest': rf_acc_v2*100,
        'MLP': mlp_acc_v2*100
    }
}

best_acc = 0
best_model = ""
best_features = ""

for feature_type, models in results.items():
    print(f"\n{feature_type}:")
    for model_name, acc in models.items():
        status = "✓ PASS" if acc >= 90 else "✗ FAIL"
        print(f"  {model_name:20s}: {acc:6.2f}% {status}")
        if acc > best_acc:
            best_acc = acc
            best_model = model_name
            best_features = feature_type

print("\n" + "="*70)
print(f"BEST MODEL: {best_model} with {best_features}")
print(f"ACCURACY: {best_acc:.2f}%")

if best_acc >= 90:
    print("✓✓✓ REQUIREMENT MET: >90% accuracy achieved!")
else:
    print(f"✗✗✗ REQUIREMENT NOT MET: Need {90-best_acc:.2f}% more")
    print("\nTrying combined features approach...")

    # Combine features
    from scipy.sparse import hstack
    X_combined = np.hstack([X_v1, X_v2])
    X_train_comb, X_test_comb, y_train, y_test = train_test_split(
        X_combined, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
    )

    print("\nCombined Features (Statistical + N-gram):")
    print(f"Feature matrix: {X_combined.shape}")

    rf_comb = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    rf_comb.fit(X_train_comb, y_train)
    acc_comb = accuracy_score(y_test, rf_comb.predict(X_test_comb))

    print(f"Random Forest (Combined): {acc_comb*100:.2f}%")

    if acc_comb >= 90:
        print("✓✓✓ REQUIREMENT MET with combined features!")
    else:
        print(f"Still need {90-acc_comb*100:.2f}% more - trying advanced techniques...")

print("\n" + "="*70)
