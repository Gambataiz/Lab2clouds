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

        N_s = [10, 100, 1000, 10000, 100000, 1000000]
        results = [0, 0, 0, 0, 0, 0]
        i=0
        for N in N_s:
            results[i] = numerical_integration(lower, upper, N)
            i = i + 1
        i=0
        return jsonify({
            "lower": lower,
            "upper": upper,
            "result for N=10": results[0],
            "result for N=100": results[1],
            "result for N=1k": results[2],
            "result for N=10k": results[3],
            "result for N=100k": results[4],
            "result for N=1M": results[5],
        }), 200
    except ValueError:
        return jsonify({"error": "Bounds must be numeric"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
