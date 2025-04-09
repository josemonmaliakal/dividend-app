<template>
  <div class="container min-dvh">    
    <div class="p-6">
      <h2 class="text-2xl font-semibold mb-4">Dividend Payouts – {{ monthName }} - {{ year }} </h2>
      <div class="overflow-x-auto bg-white shadow-md rounded-2xl">
        <table class="min-w-full text-sm text-left">
          <thead class="bg-gray-100 text-gray-700 uppercase text-xs">
            <tr>
              <th class="px-6 py-3">Company</th>
              <th class="px-6 py-3">Symbol</th>
              <th class="px-6 py-3 text-right">Dividend (₹)</th>
              <th class="px-6 py-3 text-center">Ex-Date</th>
              <th class="px-6 py-3 text-center">Record Date</th>
              <th class="px-6 py-3 text-center">Type</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="(d, i) in dividends" :key="i">
              <td  class="px-6 py-4" >{{ d.company }}</td>
              <td>{{ d.symbol }}</td>
              <td>{{ d.dividend }}</td>
              <td>{{ d.ex_date }}</td>
              <td>{{ d.record_date }}</td>
              <td>{{ d.type }}</td>
            </tr>
          </tbody>
        </table>
    </div>
  </div>   
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
  month: Number,
  year: Number,
  monthName:String
})


const dividends = ref([])



onMounted(() => {
  axios
    .get(`http://localhost:8000/api/dividends?month=${props.month}&year=${props.year}`)
    .then((res) => {
      dividends.value = res.data
    })
    .catch(console.error)
})
</script>
