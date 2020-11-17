<template>
<div>
  <ul class="contributors-list">
    <li class="contributors-item" v-for="contributor in contributors" :key="contributor.id">
      <a class="avatar_container" :href="contributor.html_url">
        <img class="avatar_image" :src="contributor.avatar_url" :alt="contributor.login">
        <a class="avatar_name">{{ contributor.login }}</a>
      </a>
    </li>
  </ul>
</div>
</template>

<script>
export default {
  props: {
    user: {
      type: String,
      require: true
    },
    repo: {
      type: String,
      require: true
    }
  },
  data () {
    return {
      contributors: []
    }
  },
  mounted () {
    this.getContributors()
  },
  methods: {
    getContributors () {
      const { user, repo } = this
      const uri = `https://api.github.com/repos/${user}/${repo}/contributors`

      fetch(uri)
      .then(function(response) {
        return response.json()
      })
      .then(res => {
        console.log(res)
        this.contributors = res
      })
    }
  }
}
</script>

<style scoped>
.contributors-list{
  display: grid;
  grid-template-columns: repeat( auto-fit, minmax(130px, 1fr) );
  flex-wrap: wrap;
  justify-items: center;
  list-style: none !important;
  margin: 0;
}

.contributors-item::before {
  display: none !important;
}

.contributors-item {
  display: inline-flex;
  list-style: none;
  margin: 0;
}

.avatar_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

.avatar_image {
  display: inline-flex;
  height: 60px;
  width: 60px;
  object-fit: cover;
  border-radius: 50%;
  margin: 0;
}
</style>
