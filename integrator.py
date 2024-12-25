from flask import Flask, jsonify, request
import math

app = Flask(__name__)

def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    total_area = 0
    for i in range(N):
        x = lower + i * dx
        total_area += abs(math.sin(x)) * dx
    return total_area

@app.route('/numericalintegralservice/<lower>/<upper>', methods=['GET'])
def integrate(lower, upper):
    try:
        lower = float(lower)
        upper = float(upper)

        N = int(request.args.get('N', 100))
        if N <= 0:
            return jsonify({"error": "N must be a positive integer"}), 400

        result = numerical_integration(lower, upper, N)
        return jsonify({
            "lower": lower,
            "upper": upper,
            "N": N,
            "result": result
        }), 200
    except ValueError:
        return jsonify({"error": "Bounds must be numeric"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
