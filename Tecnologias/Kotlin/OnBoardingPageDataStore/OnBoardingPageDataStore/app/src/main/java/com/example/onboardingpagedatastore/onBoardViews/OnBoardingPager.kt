package com.example.onboardingpagedatastore.onBoardViews

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.pager.HorizontalPager
import androidx.compose.foundation.pager.PagerState
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import com.example.onboardingpagedatastore.data.PageData
import com.google.accompanist.pager.ExperimentalPagerApi
import com.google.accompanist.pager.HorizontalPager


@OptIn(ExperimentalPagerApi::class)
@Composable
fun OnBoardingPager(
    item:List<PageData>,
    pagerState: PagerState,
    modifier: Modifier = Modifier
){
    Box(
      modifier = modifier
    ){
        Column(horizontalAlignment = Alignment.CenterHorizontally){
            HorizontalPager(state = pagerState) {

            }
            PagerIndicator(size = item.size, currentPage = pagerState.currentPage)
        }

        Box(
            modifier = Modifier.align(Alignment.BottomCenter)
        ){
            ButtonFinish(pagerState.currentPage)
        }
    }

}