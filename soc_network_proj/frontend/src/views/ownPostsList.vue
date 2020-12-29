<template>
  <div class="container">
  <h3>Own Posts</h3>
    <b-button id="create" :to="{ name: 'create-post' }" variant="info">Create Post</b-button>
    <b-alert variant="success" :show="isPostCreated" dismissible>New post was created successfully.</b-alert>
    <postList :posts="posts" />
  </div>
</template>

<script>
import postList from '@/components/post/postList.vue';

export default {
  name: "ownPostsList",
  components: {
    postList,
  },
  computed: {
    posts() {
      return this.$store.getters.posts;
    },
    isPostCreated() {
      return this.$store.getters.postEvent === 'create';
    },
  },
  beforeMount() {
    this.$store.dispatch('getPosts', { params: {'owner': 'true'}});
  }
}
</script>