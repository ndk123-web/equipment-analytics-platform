import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import type { UploadResponse } from '../../types/upload';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

interface AnalyticsChartsProps {
  uploadData: UploadResponse | null;
}

export const AnalyticsCharts: React.FC<AnalyticsChartsProps> = ({ uploadData }) => {
  if (!uploadData) {
    return (
      <div className="bg-gray-50 rounded-xl p-8 text-center">
        <p className="text-gray-500">Upload a CSV file to see analytics</p>
      </div>
    );
  }

  // Equipment Distribution Chart Data
  const equipmentLabels = Object.keys(uploadData.equipment_distribution);
  const equipmentValues = Object.values(uploadData.equipment_distribution);

  const equipmentChartData = {
    labels: equipmentLabels,
    datasets: [
      {
        label: 'Equipment Count',
        data: equipmentValues,
        backgroundColor: [
          '#3B82F6',
          '#10B981',
          '#F59E0B',
          '#EF4444',
          '#8B5CF6',
          '#EC4899',
        ],
        borderColor: [
          '#1E40AF',
          '#065F46',
          '#B45309',
          '#991B1B',
          '#6D28D9',
          '#BE185D',
        ],
        borderWidth: 2,
      },
    ],
  };

  // Average Metrics Chart Data
  const metricsChartData = {
    labels: ['Avg Power', 'Avg Usage Hours'],
    datasets: [
      {
        label: 'Metrics',
        data: [uploadData.avg_power, uploadData.avg_usage_hours],
        backgroundColor: ['#3B82F6', '#10B981'],
        borderColor: ['#1E40AF', '#065F46'],
        borderWidth: 2,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: 'top' as const,
      },
    },
  };

  return (
    <div className="space-y-6">
      {/* File Info */}
      <div className="bg-blue-50 rounded-xl p-6 border border-blue-200">
        <h3 className="text-lg font-semibold text-gray-900 mb-3">📊 File Analytics</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div>
            <p className="text-gray-600 text-sm">File Name</p>
            <p className="text-gray-900 font-semibold text-sm">{uploadData.name}</p>
          </div>
          <div>
            <p className="text-gray-600 text-sm">Total Rows</p>
            <p className="text-gray-900 font-semibold text-sm">{uploadData.total_rows}</p>
          </div>
          <div>
            <p className="text-gray-600 text-sm">Avg Power</p>
            <p className="text-gray-900 font-semibold text-sm">{uploadData.avg_power.toFixed(2)}</p>
          </div>
          <div>
            <p className="text-gray-600 text-sm">Avg Usage Hours</p>
            <p className="text-gray-900 font-semibold text-sm">{uploadData.avg_usage_hours.toFixed(2)}</p>
          </div>
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Equipment Distribution */}
        <div className="bg-white rounded-xl shadow-md p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Equipment Distribution</h3>
          <Bar data={equipmentChartData} options={chartOptions} height={300} />
        </div>

        {/* Average Metrics */}
        <div className="bg-white rounded-xl shadow-md p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Average Metrics</h3>
          <Bar data={metricsChartData} options={chartOptions} height={300} />
        </div>
      </div>
    </div>
  );
};
