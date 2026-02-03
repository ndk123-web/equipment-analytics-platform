import { Link } from 'react-router-dom';
import { SignupForm } from '../components/auth/SignupForm';

export const SignupPage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-emerald-100 flex items-center justify-center py-12 px-4">
      <div className="w-full max-w-md">
        {/* Card Container */}
        <div className="bg-white rounded-2xl shadow-xl p-8">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-gray-900 mb-2">Get Started</h1>
            <p className="text-gray-600 text-sm">Create your account and join us today</p>
          </div>

          {/* Signup Form */}
          <SignupForm />

          {/* Footer Link */}
          <div className="mt-6 text-center">
            <p className="text-gray-600 text-sm">
              Already have an account?{' '}
              <Link
                to="/login"
                className="font-semibold text-green-600 hover:text-green-700 transition"
              >
                Sign In
              </Link>
            </p>
          </div>
        </div>

        {/* Footer */}
        <p className="text-center text-gray-600 text-xs mt-6">
          By signing up, you agree to our{' '}
          <a href="#" className="text-green-600 hover:text-green-700">
            Terms of Service
          </a>{' '}
          and{' '}
          <a href="#" className="text-green-600 hover:text-green-700">
            Privacy Policy
          </a>
        </p>
      </div>
    </div>
  );
};
