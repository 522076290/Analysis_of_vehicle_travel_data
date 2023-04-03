<template>
  <div>
    <svg-icon icon-class="github" @click="goto" />
  </div>
</template>

<script>
export default {
  name: 'RuoYiGit',
  data() {
    return {
      url: 'https://github.com/522076290/Analysis_of_vehicle_travel_data'
    }
  },
  methods: {
    goto() {
      window.open(this.url)
    }
  }
}
</script>