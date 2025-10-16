package ru.vinteno.lavka.data

import com.google.gson.annotations.SerializedName

data class Order(
    @SerializedName("id")
    val id: Int,

    @SerializedName("items")
    val products: String,

    @SerializedName("delivery_address")
    val name: String,

    @SerializedName("status")
    val status: String? = "Новый",

    // Это поле может отсутствовать в API, оставляем как есть
    val dateTime: String = ""
)