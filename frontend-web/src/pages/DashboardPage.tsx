import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export const DashboardPage = () => {
  const navigate = useNavigate();
  const { user, logout } = useAuthStore();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-4xl font-bold text-gray-900">
                Welcome, {user?.first_name || 'User'}! 👋
              </h1>
              <p className="text-gray-600 mt-2">{user?.email}</p>
            </div>
            <button
              onClick={handleLogout}
              className="px-6 py-2.5 bg-red-600 text-white rounded-lg hover:bg-red-700 transition font-medium"
            >
              Logout
            </button>
          </div>
        </div>

        {/* User Info Card */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Profile Information</h2>
            <div className="space-y-4">
              <div>
                <p className="text-gray-600 text-sm">Email</p>
                <p className="text-gray-900 font-medium">{user?.email}</p>
              </div>
              <div>
                <p className="text-gray-600 text-sm">Name</p>
                <p className="text-gray-900 font-medium">
                  {user?.first_name} {user?.last_name}
                </p>
              </div>
              <div>
                <p className="text-gray-600 text-sm">User ID</p>
                <p className="text-gray-900 font-medium">{user?.id}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl shadow-lg p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h2>
            <div className="space-y-3">
              <button className="w-full py-2.5 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition font-medium">
                Edit Profile
              </button>
              <button className="w-full py-2.5 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition font-medium">
                Change Password
              </button>
              <button className="w-full py-2.5 px-4 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition font-medium">
                Settings
              </button>
            </div>
          </div>
        </div>

        {/* Features Section */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mt-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
              <h3 className="font-semibold text-gray-900">✨ Modern UI</h3>
              <p className="text-gray-600 text-sm mt-1">Built with React & Tailwind CSS</p>
            </div>
            <div className="p-4 bg-green-50 rounded-lg border border-green-200">
              <h3 className="font-semibold text-gray-900">🔒 Secure Auth</h3>
              <p className="text-gray-600 text-sm mt-1">JWT token-based authentication</p>
            </div>
            <div className="p-4 bg-purple-50 rounded-lg border border-purple-200">
              <h3 className="font-semibold text-gray-900">💾 Persistent State</h3>
              <p className="text-gray-600 text-sm mt-1">LocalStorage integration with Zustand</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
