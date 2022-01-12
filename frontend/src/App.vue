<template>
  <v-app>
    <v-container class="py-10">
      <v-row align="start" justify="start">
        <v-col cols="6">
          <twitter-search-bar
            @toggle-searching="isSearching = $event"
            @update-tweet-list="tweetList = $event"
          ></twitter-search-bar>
        </v-col>
      </v-row>

      <v-row align="center" justify="center">
        <v-col cols="6">
          <tweet-list
            :is-searching="isSearching"
            :tweet-list="tweetList"
            :translate-lang-value="translateLangValue"
            @toggle-translating="isTranslating = $event"
            @update-translated-data="translatedData = $event"
          ></tweet-list>
        </v-col>

        <v-col cols="1">
          <v-icon large>
            mdi-chevron-right
          </v-icon>
        </v-col>

        <v-col cols="5" align-self="start">
          <translation-display
            :translated-data="translatedData"
            :is-translating="isTranslating"
            @update-translate-lang-value="translateLangValue = $event"
          ></translation-display>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import TwitterSearchBar from './components/TwitterSearchBar.vue'
import TweetList from './components/TweetList.vue'
import TranslationDisplay from './components/TranslationDisplay.vue'

export default {
  components: { TwitterSearchBar, TweetList, TranslationDisplay },
  name: 'App',

  data () {
    return {
      tweetList: [],
      isSearching: false,
      translateLangValue: 'JA',
      isTranslating: false,
      translatedData: { text: '' }
    }
  }
}
</script>
