# Explicación proyecto / Practica

This project is a way to see the diferents way to implement viewmodel

## ViewModel + State

### Example:

Uses Kotlin coroutines + Flow for reactive state handling

```
class CounterViewModel : ViewModel() {
    private val _count = MutableStateFlow(0)
    val count: StateFlow<Int> get() = _count

    fun increment() {
        _count.value++
    }
}

```

In Jetpack Compose:

```
    val count by viewModel.count.collectAsState()
    Text("Count: $count")
```


- Pros: Modern, supports async, works great with Compose
- Cons: Slightly steeper learning curve than LiveData

## SavedStateHandle + viewmodel

Useful when you need state to survive process death or store navigation arguments.

### Example:


```
class ProfileViewModel(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    val userId: String = savedStateHandle["userId"] ?: "unknown"

    fun saveScrollPosition(pos: Int) {
        savedStateHandle["scrollPosition"] = pos
    }

    fun getScrollPosition(): Int = savedStateHandle["scrollPosition"] ?: 0
}

``` 


-Pros: Survives process death, built-in with Navigation Component
-Cons: Not always needed if your state is transient

### Note:

For this project and serialize elements in the build.gradle.kts (Module:app) it was added
in the plugins

```
id("kotlin-parcelize")

```









