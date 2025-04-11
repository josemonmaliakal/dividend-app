<template>
  <div class="grow p-6 lg:rounded-lg lg:bg-white lg:p-10 lg:ring-1 lg:shadow-xs lg:ring-zinc-950/5 dark:lg:bg-zinc-900 dark:lg:ring-white/10">
    <div class="mx-auto max-w-6xl">
      <div class="flex items-end justify-between gap-4">
        <h1 class="text-2xl/8 font-semibold text-zinc-950 sm:text-xl/8 dark:text-white">
          Dividend Payouts | {{ selectedMonthName }}  {{ selectedYear }}
        </h1>
        <div class="flex gap-4">
          <select v-model="selectedMonth" @change="fetchDividends" class="border rounded p-2">
            <option v-for="(m, idx) in months" :key="idx" :value="idx + 1">{{ m }}</option>
          </select>        
          <select v-model="selectedYear" @change="fetchDividends" class="border rounded p-2">
            <option v-for="y in years" :key="y" :value="y">{{ y }}</option>
          </select>
        </div>
      </div>
      <div class="flow-root">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200 text-sm">
            <thead class="bg-gray-100">
              <tr>
                <th class="px-6 py-3 text-left font-medium text-gray-700">COMPANY</th>
                <th class="px-6 py-3 text-left font-medium text-gray-700">SYMBOL</th>
                <th class="px-6 py-3 text-left font-medium text-gray-700">DIVIDEND (₹)</th>
                <th class="px-6 py-3 text-left font-medium text-gray-700">EX-DATE</th>
                <th class="px-6 py-3 text-left font-medium text-gray-700">RECORD DATE</th>
                <th class="px-6 py-3 text-left font-medium text-gray-700">TYPE</th>
                <th class="px-6 py-3 text-center">More</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">          
              <template v-for="(d, i) in dividends" :key="i">
              <!-- Main Row -->
              <tr @click="toggleExpanded(i)" class="cursor-pointer hover:bg-gray-50">
                <td class="px-6 py-4">{{ d.company }}</td>
                <td>{{ d.symbol }}</td>
                <td class="text-right">{{ d.dividend }}</td>
                <td class="text-center">{{ formatDate(d.ex_date) }}</td>
                <td class="text-center">{{ formatDate(d.record_date) }}</td>
                <td class="text-center">{{ d.type }}</td>
                <td class="text-center text-blue-500">▼</td>
              </tr>

              <!-- Expanded Row -->
              <tr v-if="expandedRow === i">
                <td colspan="7" class="px-6 pb-4 pt-2 bg-gray-50">
                  <Suspense>
                    <template #default>
                      <LazyChart :history="d.history" />
                    </template>
                    <template #fallback>
                      <p>Loading chart...</p>
                    </template>
                  </Suspense>
                </td>
              </tr>
            </template>
            </tbody>
          </table>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>

import { ref, computed, onMounted , defineAsyncComponent} from 'vue'
import axios from 'axios'
import DividendChart from '@/components/DividendChart.vue'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
]

const years = Array.from({ length: 10 }, (_, i) => new Date().getFullYear() - i)

const selectedMonth = ref(new Date().getMonth() + 1)
const selectedYear = ref(new Date().getFullYear())

const selectedMonthName = computed(() => months[selectedMonth.value - 1])



// State
const dividends = ref([])

const expandedRow = ref(0) 
// Lazy component
const LazyChart = defineAsyncComponent(() => import('@/components/DividendChart.vue'))


// Toggle
const toggleExpanded = (index) => {
  expandedRow.value = expandedRow.value === index ? null : index
}



const formatDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return new Intl.DateTimeFormat('en-GB', {
    day: '2-digit',
    month: 'long',
    year: 'numeric'
  }).format(date)
}

const fetchDividends = () => {
  axios
    .get(`${API_BASE_URL}/api/dividends?month=${selectedMonth.value}&year=${selectedYear.value}`)
    .then((res) => {
      dividends.value = res.data
    })
    .catch(console.error)
}

onMounted(fetchDividends)
</script>