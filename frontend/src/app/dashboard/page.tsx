// frontend/src/app/dashboard/page.tsx
import ProtectedRoute from "@/components/ProtectedRoute";
import Link from "next/link";

export default function DashboardPage() {
    return (
        <ProtectedRoute>
            <div className="text-center">
                <h1 className="text-3xl font-bold mb-4">Welcome to your Dashboard</h1>
                <p className="text-lg mb-6">You are successfully logged in.</p>
                <Link 
                    href="/tasks"
                    className="bg-blue-500 text-white px-6 py-3 rounded-lg font-semibold text-lg hover:bg-blue-600 transition-colors"
                >
                    Go to My Tasks
                </Link>
            </div>
        </ProtectedRoute>
    );
}
