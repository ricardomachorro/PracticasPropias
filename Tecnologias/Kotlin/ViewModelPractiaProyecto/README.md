# Explicación proyecto / Practica

This projet is a way to see the diferents way to implement viewmodel

## ViewModel + State

### Example:

Uses Kotlin coroutines + Flow for reactive state handling


class CounterViewModel : ViewModel() {
    private val _count = MutableStateFlow(0)
    val count: StateFlow<Int> get() = _count

    fun increment() {
        _count.value++
    }
}


In Jetpack Compose:


    val count by viewModel.count.collectAsState()
    Text("Count: $count")



- Pros: Modern, supports async, works great with Compose
- Cons: Slightly steeper learning curve than LiveData




