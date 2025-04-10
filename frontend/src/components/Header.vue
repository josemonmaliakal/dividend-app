<template>
  <header class="bg-white">
    <div class="sticky top-0 z-10 border-b border-zinc-950/10 bg-white px-6 py-5 sm:px-8 lg:z-10 lg:flex lg:h-16 lg:items-center lg:py-0 dark:border-white/10 dark:bg-zinc-900">
      <div class="mx-auto flex w-full max-w-xl items-center justify-between lg:max-w-7xl">
        <div class="flex items-center gap-2 sm:gap-4">
          <a aria-label="Home" href="/">
            <b>QueryB</b>
          </a>
        </div>
        <div class="flex items-center gap-4 sm:gap-8">
          <a class="text-sm/6 font-medium text-zinc-700 hover:text-zinc-950 dark:text-zinc-300 dark:hover:text-white" href="#">Home <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </div>    
  </header>
</template>

<script setup>
import { ref } from 'vue'
import {
  Dialog,
  DialogPanel,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Popover,
  PopoverButton,
  PopoverGroup,
  PopoverPanel,
} from '@headlessui/vue'
import {
  ArrowPathIcon,
  Bars3Icon,
  ChartPieIcon,
  CursorArrowRaysIcon,
  FingerPrintIcon,
  SquaresPlusIcon,
  XMarkIcon,
} from '@heroicons/vue/24/outline'
import { ChevronDownIcon, PhoneIcon, PlayCircleIcon } from '@heroicons/vue/20/solid'

const products = [
  { name: 'Analytics', description: 'Get a better understanding of your traffic', href: '#', icon: ChartPieIcon },
  { name: 'Engagement', description: 'Speak directly to your customers', href: '#', icon: CursorArrowRaysIcon },
  { name: 'Security', description: 'Your customers’ data will be safe and secure', href: '#', icon: FingerPrintIcon },
  { name: 'Integrations', description: 'Connect with third-party tools', href: '#', icon: SquaresPlusIcon },
  { name: 'Automations', description: 'Build strategic funnels that will convert', href: '#', icon: ArrowPathIcon },
]
const callsToAction = [
  { name: 'Watch demo', href: '#', icon: PlayCircleIcon },
  { name: 'Contact sales', href: '#', icon: PhoneIcon },
]

const mobileMenuOpen = ref(false)
</script>