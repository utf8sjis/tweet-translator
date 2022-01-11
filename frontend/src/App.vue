<template>
  <v-app>
    <v-container
      class="py-10"
    >
      <v-row align="start" justify="start">
        <v-col cols="6">
          <v-row align="center" justify="center">
            <v-col cols="7">
              <v-text-field
                label="検索したい言葉を入力してください"
                v-model="searchWord"
              ></v-text-field>
            </v-col>
            <v-col cols="3">
              <v-select
                v-model="searchLang"
                :hint="`lang:${searchLang.value}`"
                :items="searchLangItems"
                item-text="lang"
                item-value="value"
                label="Select"
                persistent-hint
                return-object
                single-line
              ></v-select>
            </v-col>
            <v-col cols="2">
              <v-btn
                outlined
                @click="searchTweets()"
                block
                color="cyan"
              >検索</v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <v-row align="center" justify="center">
        <v-col cols="6">

          <v-toolbar
            color="cyan"
            dark
          >
            <v-toolbar-title>
              <v-icon
                large
                left
              >
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
                            >翻訳</v-btn>
                          </v-row>
                        </v-list-item>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </template>
            </v-container>
          </v-card>
        </v-col>

        <v-col cols="1">
          <v-icon
            large
          >
            mdi-chevron-right
          </v-icon>
        </v-col>

        <v-col cols="5" align-self="start">
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="translateLang"
                  :items="translateLangItems"
                  item-text="lang"
                  item-value="value"
                  label="Select"
                  prepend-icon="mdi-translate"
                  return-object
                  single-line
                ></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-card
                  :loading="isTranslating"
                >
                  <v-card-text>
                    {{ translatedData.text }}
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  data () {
    return {
      searchWord: '',
      searchLang: { lang: '英語', value: 'en' },
      searchLangItems: [
        { lang: '日本語', value: 'ja' },
        { lang: '英語', value: 'en' }
      ],
      isSearching: false,
      tweetList: [],
      translateLang: { lang: '日本語', value: 'JA' },
      translateLangItems: [
        { lang: '日本語', value: 'JA' },
        { lang: '英語', value: 'EN-US' }
      ],
      isTranslating: false,
      translatedData: {}
    }
  },

  methods: {
    /**
     * 検索
     */
    searchTweets: function () {
      this.isSearching = true

      var data = {
        searchWord: this.searchWord,
        searchLang: this.searchLang.value
      }

      axios
        .post('/api/twitter/search', data)
        .then((response) => {
          this.tweetList = response.data
          this.isSearching = false
        })
        .catch((err) => {
          alert('APIサーバの接続に失敗しました')
          this.isSearching = false
          err = null
        })
    },
    /**
     * 翻訳
     */
    translateTweet: function (tweetText) {
      this.isTranslating = true

      var data = {
        tweetText: tweetText,
        translateLang: this.translateLang.value
      }

      axios
        .post('/api/deepl/translate', data)
        .then((response) => {
          this.translatedData = response.data
          this.isTranslating = false
        })
        .catch((err) => {
          this.isTranslating = false
          alert('APIサーバの接続に失敗しました')
          err = null
        })
    }
  }
}
</script>
