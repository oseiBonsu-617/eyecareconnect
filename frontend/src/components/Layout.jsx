import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Layout({ children }) {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4 flex justify-between">
        <span className="font-semibold">EyeCareConnect</span>
        {user && (
          <div className="flex gap-4 items-center">
            <span>{user.username}</span>
            <button
              onClick={handleLogout}
              className="bg-red-500 px-3 py-1 rounded"
            >
              Logout
            </button>
          </div>
        )}
      </header>

      <main className="p-6">{children}</main>
    </div>
  );
}
