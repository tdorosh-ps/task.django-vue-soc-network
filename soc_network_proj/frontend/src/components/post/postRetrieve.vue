<template>
<b-card :title="post.title">
  <b-card-text>
    {{ post.body }}
  </b-card-text>
  <h6>Likes <b-badge>{{ likes }}</b-badge></h6>
  <h6>Author <b-badge>{{ post.owner.email }}</b-badge></h6>
  <h6>Created <b-badge>{{ post.created }}</b-badge></h6>
  <h6>Modified <b-badge>{{ post.modified }}</b-badge></h6>
  <template v-if="!isOwner">
    <b-button id="like" v-if="!liked" @click="changePostLikes('like')" variant="primary">Like</b-button>
    <b-button id="unlike" v-else-if="liked" @click="changePostLikes('unlike')" variant="primary">UnLike</b-button>
  </template>
</b-card>
</template>

<script>
export default {
  name: "postRetrieve",
  computed: {
    post() {
      return this.$store.getters.post;
    },
    likes() {
      return this.$store.getters.post.users_liked.length;
    },
    authUser() {
      return this.$store.getters.authUser[0];
    },
    isOwner() {
      return this.$store.getters.post.owner.id === this.authUser.id;
    },
    users_liked_ids() {
      const users_liked_ids = [];
      this.$store.getters.post.users_liked.forEach((user) => {
        users_liked_ids.push(user.id);
      })
      return users_liked_ids
    },
    liked() {
      return this.users_liked_ids.includes(this.authUser.id);
    }
  },
  methods: {
    changePostLikes(action) {
      const postLikeData = {
        post: {
          id: this.post.id,
          owner: this.post.owner,
          users_liked: this.post.users_liked,
        },
        data: {
          action: action,
        }
      }
      this.$store.dispatch('likePost', postLikeData);
    }
  },
  beforeMount() {
    this.$store.dispatch('getPost', this.$route.params.id);
    this.$store.dispatch('getUser');
  },
}
</script>
