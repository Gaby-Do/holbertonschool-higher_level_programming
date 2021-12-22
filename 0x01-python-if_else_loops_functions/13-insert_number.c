#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to a linked list
 * @number: number to be inserted
 * Return: pointer to new node, NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *aux = NULL, *prox = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		*head = new;
		return (*head);
	}
	if (number <= (*head)->n)
	{
		new->next = *head;
		return (*head = new);
	}
	aux = *head;
	prox = aux->next;
	while (prox)
	{
		if (prox->n >= number)
			break;
		aux = prox;
		prox = prox->next;
	}
	aux->next = new;
	new->next = prox;
	return (new);
}
