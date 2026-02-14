from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import joblib
import numpy as np
import os
from django.conf import settings

# Load model at module level (loads once)
BASE_DIR = settings.BASE_DIR
MODEL_PATH = os.path.join(BASE_DIR, 'house_price_model.pkl')

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None


@login_required
def predict_view(request):
    """ML prediction view"""
    prediction = None
    input_value = None
    error_message = None
    
    if request.method == 'POST':
        try:
            # Get input from form
            input_value = float(request.POST.get('area', 0))
            
            if model is None:
                error_message = "Model not loaded. Please contact administrator."
            elif input_value <= 0:
                error_message = "Please enter a valid area greater than 0."
            else:
                # Make prediction
                input_array = np.array([[input_value]])
                prediction_value = model.predict(input_array)[0]
                prediction = f"${prediction_value:,.2f}"
                
        except ValueError:
            error_message = "Invalid input! Please enter a number."
        except Exception as e:
            error_message = f"Prediction error: {str(e)}"
    
    context = {
        'prediction': prediction,
        'input_value': input_value,
        'error_message': error_message,
        'user': request.user,
    }
    
    return render(request, 'ml_predict/predict.html', context)