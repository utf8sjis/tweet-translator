<template>
  <div>
    <v-toolbar dark color="cyan">
      <v-toolbar-title>
        <v-icon large left>
          mdi-twitter
        </v-icon>
        <span class="text-h6 font-weight-light">Tweets</span>
      </v-toolbar-title>
    </v-toolbar>

    <v-card
      class="overflow-auto rounded-t-0"
      height="500"
      :loading="isSearching"
    >
      <v-container>
        <template v-for="tweet in tweetList">
          <v-row :key="tweet.tweetId">
            <v-col>
              <v-card>
                <v-card-title>
                  <v-list-item class="px-0">
                    <v-list-item-avatar>
                      <v-img
                        alt=""
                        :src="tweet.userProfileImageUrl"
                      ></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title class="flex-shrink-0">
                        {{ tweet.userName }}
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        @{{ tweet.userScreenName }}
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-card-title>

                <v-card-text>
                  {{ tweet.tweetText }}
                </v-card-text>

                <v-card-actions>
                  <v-list-item class="grow">
                    <v-row align="center" justify="end">
                      <v-btn
                        color="blue darken-1 white--text"
                        @click="translateTweet(tweet.tweetText)"
                      >
                        翻訳
                      </v-btn>
                    </v-row>
                  </v-list-item>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </template>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TweetList',

  props: {
    isSearching: Boolean,
    tweetList: Array,
    translateLangValue: String
  },

  data: () => ({
  }),

  methods: {
    /**
     * 翻訳
     */
    translateTweet: function (tweetText) {
      this.$emit('toggle-translating', true)

      var data = {
        tweetText: tweetText,
        translateLang: this.translateLangValue
      }

      axios
        .post('/api/deepl/translate', data)
        .then((response) => {
          this.$emit('update-translated-data', response.data)
          this.$emit('toggle-translating', false)
        })
        .catch((err) => {
          alert('APIサーバの接続に失敗しました')
          this.$emit('update-translated-data', { text: '' })
          this.$emit('toggle-translating', false)
          err = null
        })
    }
  }
}
</script>
