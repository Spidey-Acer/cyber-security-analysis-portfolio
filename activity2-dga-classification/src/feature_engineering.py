"""
Feature Engineering Utilities for DGA Classification
Activity 2 - Cyber Security Analytics

This module provides helper functions for extracting features from domain names.
"""

import numpy as np
import pandas as pd
from collections import Counter
import re


def calculate_entropy(text):
    """
    Calculate Shannon entropy of a string.
    Higher entropy = more random/unpredictable
    
    Args:
        text (str): Input string
        
    Returns:
        float: Entropy value
    """
    if not text:
        return 0
    
    # Count character frequencies
    char_freq = Counter(text.lower())
    length = len(text)
    
    # Calculate entropy
    entropy = -sum((count/length) * np.log2(count/length) 
                   for count in char_freq.values() if count > 0)
    
    return entropy


def get_character_diversity(text):
    """
    Calculate the ratio of unique characters to total characters.
    
    Args:
        text (str): Input string
        
    Returns:
        float: Diversity ratio (0-1)
    """
    if not text:
        return 0
    return len(set(text)) / len(text)


def count_consecutive_chars(text):
    """
    Count maximum consecutive repeated characters.
    DGA domains often have fewer consecutive repeated characters.
    
    Args:
        text (str): Input string
        
    Returns:
        int: Maximum consecutive character count
    """
    if not text:
        return 0
    
    import itertools
    max_consecutive = max((sum(1 for _ in group) 
                          for char, group in itertools.groupby(text)), 
                          default=0)
    return max_consecutive


def analyze_ngrams(text, n=2):
    """
    Extract n-gram statistics from text.
    
    Args:
        text (str): Input string
        n (int): N-gram size (2 for bigrams, 3 for trigrams)
        
    Returns:
        dict: N-gram statistics
    """
    text = text.lower()
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    
    if not ngrams:
        return {'unique_ratio': 0, 'most_common_freq': 0}
    
    ngram_counts = Counter(ngrams)
    unique_ratio = len(ngram_counts) / len(ngrams)
    most_common_freq = ngram_counts.most_common(1)[0][1] / len(ngrams)
    
    return {
        'unique_ratio': unique_ratio,
        'most_common_freq': most_common_freq
    }


def extract_linguistic_features(domain):
    """
    Extract linguistic and statistical features from a domain name.
    
    Args:
        domain (str): Domain name
        
    Returns:
        dict: Dictionary of features
    """
    domain_lower = domain.lower()
    length = len(domain)
    
    # Basic character counts
    alpha_count = sum(c.isalpha() for c in domain)
    digit_count = sum(c.isdigit() for c in domain)
    special_count = sum(not c.isalnum() for c in domain)
    
    # Vowel/consonant analysis
    vowels = 'aeiou'
    vowel_count = sum(c in vowels for c in domain_lower)
    consonant_count = alpha_count - vowel_count
    
    # Calculate ratios
    alpha_ratio = alpha_count / length if length > 0 else 0
    digit_ratio = digit_count / length if length > 0 else 0
    vowel_ratio = vowel_count / length if length > 0 else 0
    consonant_ratio = consonant_count / length if length > 0 else 0
    
    # Entropy and diversity
    entropy = calculate_entropy(domain_lower)
    diversity = get_character_diversity(domain_lower)
    
    # Consecutive characters
    max_consecutive = count_consecutive_chars(domain_lower)
    
    # N-gram analysis
    bigram_stats = analyze_ngrams(domain_lower, n=2)
    trigram_stats = analyze_ngrams(domain_lower, n=3)
    
    # Check for common patterns
    has_hyphen = '-' in domain
    has_number = digit_count > 0
    starts_with_digit = domain[0].isdigit() if domain else False
    ends_with_digit = domain[-1].isdigit() if domain else False
    
    return {
        # Basic metrics
        'length': length,
        'alpha_count': alpha_count,
        'digit_count': digit_count,
        'special_count': special_count,
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        
        # Ratios
        'alpha_ratio': alpha_ratio,
        'digit_ratio': digit_ratio,
        'vowel_ratio': vowel_ratio,
        'consonant_ratio': consonant_ratio,
        
        # Statistical measures
        'entropy': entropy,
        'diversity': diversity,
        'max_consecutive': max_consecutive,
        
        # N-gram features
        'bigram_unique_ratio': bigram_stats['unique_ratio'],
        'bigram_most_common_freq': bigram_stats['most_common_freq'],
        'trigram_unique_ratio': trigram_stats['unique_ratio'],
        'trigram_most_common_freq': trigram_stats['most_common_freq'],
        
        # Pattern features
        'has_hyphen': int(has_hyphen),
        'has_number': int(has_number),
        'starts_with_digit': int(starts_with_digit),
        'ends_with_digit': int(ends_with_digit)
    }


def extract_features_batch(domains):
    """
    Extract features for multiple domains efficiently.
    
    Args:
        domains (list): List of domain names
        
    Returns:
        pd.DataFrame: Feature matrix
    """
    features_list = []
    
    for domain in domains:
        features = extract_linguistic_features(domain)
        features_list.append(features)
    
    return pd.DataFrame(features_list)


def get_vowel_consonant_pattern(domain):
    """
    Encode domain as vowel/consonant pattern.
    Example: "google" -> "CVVCVC" (C=consonant, V=vowel)
    
    Args:
        domain (str): Domain name
        
    Returns:
        str: Pattern string
    """
    vowels = 'aeiou'
    pattern = ''
    
    for char in domain.lower():
        if char.isalpha():
            pattern += 'V' if char in vowels else 'C'
        elif char.isdigit():
            pattern += 'D'
        else:
            pattern += 'S'
    
    return pattern


def calculate_pronounceability_score(domain):
    """
    Estimate how pronounceable a domain is.
    DGA domains tend to be less pronounceable.
    
    Based on vowel distribution and consonant clusters.
    
    Args:
        domain (str): Domain name
        
    Returns:
        float: Pronounceability score (0-1)
    """
    domain_lower = domain.lower()
    vowels = 'aeiou'
    
    if not domain_lower:
        return 0
    
    # Check for reasonable vowel distribution
    vowel_positions = [i for i, c in enumerate(domain_lower) if c in vowels]
    
    if not vowel_positions:
        return 0  # No vowels = unpronounceable
    
    # Calculate average distance between vowels
    if len(vowel_positions) > 1:
        vowel_distances = [vowel_positions[i+1] - vowel_positions[i] 
                          for i in range(len(vowel_positions)-1)]
        avg_vowel_distance = sum(vowel_distances) / len(vowel_distances)
    else:
        avg_vowel_distance = len(domain_lower)
    
    # Score based on vowel distribution (ideal distance: 2-3 chars)
    distance_score = 1 / (1 + abs(avg_vowel_distance - 2.5))
    
    # Check for excessive consonant clusters
    consonant_clusters = re.findall(r'[^aeiou]{4,}', domain_lower)
    cluster_penalty = len(consonant_clusters) * 0.2
    
    final_score = max(0, distance_score - cluster_penalty)
    
    return final_score


def extract_advanced_features(domain):
    """
    Extract advanced features for improved classification.
    
    Args:
        domain (str): Domain name
        
    Returns:
        dict: Advanced features
    """
    basic_features = extract_linguistic_features(domain)
    
    # Add advanced features
    pattern = get_vowel_consonant_pattern(domain)
    pronounceability = calculate_pronounceability_score(domain)
    
    # Pattern-based features
    pattern_length = len(pattern)
    pattern_diversity = len(set(pattern)) / pattern_length if pattern_length > 0 else 0
    
    # Combine all features
    advanced = {
        'vc_pattern_length': pattern_length,
        'vc_pattern_diversity': pattern_diversity,
        'pronounceability_score': pronounceability
    }
    
    return {**basic_features, **advanced}


# Example usage
if __name__ == "__main__":
    # Test domains
    test_domains = [
        "google.com",      # Legitimate
        "xjksdlfj.com",    # DGA-like
        "facebook.com",    # Legitimate
        "qwertyzxcv.net"   # DGA-like
    ]
    
    print("Feature Extraction Examples:\n")
    
    for domain in test_domains:
        domain_clean = domain.replace('.com', '').replace('.net', '')
        features = extract_advanced_features(domain_clean)
        
        print(f"Domain: {domain}")
        print(f"  Length: {features['length']}")
        print(f"  Entropy: {features['entropy']:.3f}")
        print(f"  Pronounceability: {features['pronounceability_score']:.3f}")
        print(f"  Vowel ratio: {features['vowel_ratio']:.3f}")
        print()