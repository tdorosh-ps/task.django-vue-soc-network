<template>
  <div class="container">
  <h3>All Posts</h3>
    <postList :posts="posts" />
  </div>
</template>

<script>
import postList from '@/components/post/postList.vue';

export default {
  name: "allPostsList",
  components: {
    postList,
  },
  computed: {
    posts() {
      return this.$store.getters.posts;
    },
  },
  beforeMount() {
    this.$store.dispatch('getPosts', { params: {'owner': 'false'}});
  }
}
</script>