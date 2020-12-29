<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand>Posts App</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse v-if="isAuthenticated" id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'all-posts' }">All Posts</b-nav-item>
          <b-nav-item :to="{ name: 'own-posts' }">Own Posts</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item>Hello, user</b-nav-item>
          <b-nav-item id="logout" @click="logout">Logout</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'navigationBar',
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('authLogout')
      .then(() => {
        this.$router.push('/signin');
      });
    },
  }
}
</script>