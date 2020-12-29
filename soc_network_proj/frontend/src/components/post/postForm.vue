<template>
  <div>
    <b-alert v-if="eventError" v-model="eventError" variant="danger" dismissible>{{ eventError }}</b-alert>
    <b-form @submit="onSubmit">
      <b-form-group label="Title" label-for="title">
        <b-form-input
          id="title"
          v-model="form.title"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Body" label-for="body">
        <b-form-textarea
          id="body"
          v-model="form.body"
          rows="3"
          max-rows="6"
          required
        ></b-form-textarea>
      </b-form-group>

      <b-button id="submit" type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: "postForm",
  data() {
    return {
      form: {
        title: null,
        body: null,
      },
      eventError: '',
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const data = {
        title: this.form.title,
        body: this.form.body,
      };
      this.$store.dispatch('createPost', data)
        .then(() => {
          router.push('/posts/own');
        }, (error) => {
            this.eventError = error.response.data;
        });
    },
  },
}
</script>