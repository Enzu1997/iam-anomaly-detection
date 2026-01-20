import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def generate_login_data(n_samples=1000):
    np.random.seed(42)

    # Generate normal login hours (work hours: 9 AM - 5 PM)
    normal_hours = np.random.normal(loc=12, scale=3, size=int(n_samples * 0.9))
    normal_hours = np.clip(normal_hours, 0, 23)

    # Generate anomalous login hours (late night/early morning)
    anomaly_hours = np.random.uniform(0, 5, size=int(n_samples * 0.1))  # FIXED: uniform (not unifrom)

    # Combine normal and anomalous hours
    hours = np.concatenate([normal_hours, anomaly_hours])

    # Generate location data
    normal_locations = np.random.choice(['Office_A', 'Office_B', 'Home'], size=int(n_samples * 0.9))
    anomaly_locations = np.random.choice(['Foreign_IP', 'Unknown'], size=int(n_samples * 0.1))
    locations = np.concatenate([normal_locations, anomaly_locations])

    # Generate failed login attempts
    failed_attempts = np.concatenate([
        np.random.poisson(lam=0.5, size=int(n_samples * 0.9)),
        np.random.poisson(lam=5, size=int(n_samples * 0.1))
    ])

    # Generate session duration (in minutes)
    session_duration = np.concatenate([
        np.random.normal(loc=120, scale=30, size=int(n_samples * 0.9)),
        np.random.uniform(5, 20, size=int(n_samples * 0.1))
    ])

    # Create DataFrame (data table)
    df = pd.DataFrame({
        'user_id': [f'user_{i%100}' for i in range(n_samples)],
        'login_hour': hours,
        'location_risk_score': [1 if loc in ['Foreign_IP', 'Unknown'] else 0 for loc in locations],
        'failed_attempts': failed_attempts,  # FIXED: underscore (not space)
        'session_duration': session_duration,
        'timestamp': [datetime.now() - timedelta(days=i) for i in range(n_samples)]
    })
    
    return df


def train_anomaly_detector(df):
    # Select features for the model
    features = ['login_hour', 'location_risk_score', 'failed_attempts', 'session_duration']
    X = df[features]

    # Train Isolation Forest model
    model = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly'] = model.fit_predict(X)
    df['anomaly_score'] = model.score_samples(X)

    # Convert predictions to boolean (True/False)
    df['is_anomaly'] = df['anomaly'] == -1
    
    return df, model


def visualize_anomalies(df):
    # Create a figure with 4 subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Login hours - FIXED: Added missing scatter plots
    axes[0, 0].scatter(df[df['is_anomaly']==False].index, 
                       df[df['is_anomaly']==False]['login_hour'], 
                       c='green', alpha=0.5, label='Normal')
    axes[0, 0].scatter(df[df['is_anomaly']==True].index, 
                       df[df['is_anomaly']==True]['login_hour'], 
                       c='red', alpha=0.7, label='Anomaly')
    axes[0, 0].set_xlabel('Login Event')
    axes[0, 0].set_ylabel('Hour of Day')
    axes[0, 0].set_title('Login Time Anomalies')
    axes[0, 0].legend()

    # Plot 2: Failed attempts
    axes[0, 1].scatter(df[df['is_anomaly']==False].index, 
                       df[df['is_anomaly']==False]['failed_attempts'], 
                       c='green', alpha=0.5, label='Normal')
    axes[0, 1].scatter(df[df['is_anomaly']==True].index, 
                       df[df['is_anomaly']==True]['failed_attempts'], 
                       c='red', alpha=0.7, label='Anomaly')
    axes[0, 1].set_xlabel('Login Event')
    axes[0, 1].set_ylabel('Failed Attempts')
    axes[0, 1].set_title('Failed Login Attempts')
    axes[0, 1].legend()

    # Plot 3: Session duration
    axes[1, 0].scatter(df[df['is_anomaly']==False].index, 
                       df[df['is_anomaly']==False]['session_duration'], 
                       c='green', alpha=0.5, label='Normal')
    axes[1, 0].scatter(df[df['is_anomaly']==True].index, 
                       df[df['is_anomaly']==True]['session_duration'], 
                       c='red', alpha=0.7, label='Anomaly')
    axes[1, 0].set_xlabel('Login Event')
    axes[1, 0].set_ylabel('Session Duration (min)')
    axes[1, 0].set_title('Session Duration Anomalies')
    axes[1, 0].legend()

    # Plot 4: Anomaly score distribution
    axes[1, 1].hist(df[df['is_anomaly']==False]['anomaly_score'], 
                    bins=50, alpha=0.5, color='green', label='Normal')
    axes[1, 1].hist(df[df['is_anomaly']==True]['anomaly_score'], 
                    bins=50, alpha=0.5, color='red', label='Anomaly')
    axes[1, 1].set_xlabel('Anomaly Score')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Anomaly Score Distribution')
    axes[1, 1].legend()

    plt.tight_layout()
    plt.savefig('iam_anomaly_detection_results.png', dpi=300, bbox_inches='tight')
    plt.show()


def generate_report(df):
    anomalies = df[df['is_anomaly']==True]
    
    print("="*60)
    print("IAM ANOMALY DETECTION REPORT")
    print("="*60)
    print(f"\nTotal login events analyzed: {len(df)}")
    print(f"Anomalies detected: {len(anomalies)} ({len(anomalies)/len(df)*100:.2f}%)")
    print(f"\nTop 10 High-Risk Users:")
    print("-"*60)
    
    user_risk = anomalies.groupby('user_id').size().sort_values(ascending=False).head(10)
    for user, count in user_risk.items():
        print(f"{user}: {count} anomalous events")
    
    print(f"\nCommon Anomaly Patterns:")
    print("-"*60)
    print(f"Off-hours logins (0-6 AM): {len(anomalies[anomalies['login_hour'] < 6])}")
    print(f"High-risk locations: {int(anomalies['location_risk_score'].sum())}")
    print(f"Excessive failed attempts: {len(anomalies[anomalies['failed_attempts'] > 3])}")
    print(f"Suspicious short sessions: {len(anomalies[anomalies['session_duration'] < 30])}")
    
    return anomalies


if __name__ == "__main__":
    print("Generating synthetic IAM login data...")
    df = generate_login_data(n_samples=1000)
    
    print("Training anomaly detection model...")
    df, model = train_anomaly_detector(df)
    
    print("Visualizing results...")
    visualize_anomalies(df)
    
    print("\nGenerating report...")
    anomalies = generate_report(df)
    
    # Save results
    anomalies.to_csv('detected_anomalies.csv', index=False)  # FIXED: Removed extra period
    print("\n✅ Anomalies saved to 'detected_anomalies.csv'")
    print("✅ Visualization saved to 'iam_anomaly_detection_results.png'")
    print("\n🎉 Project completed successfully!")