# Git Exercises

In the following small exercises, you will see how we can rewrite history of our commits.

At the beginning of each exercise, create a new branch from `main` branch named `<exercise-name>/<username>`.

```bash
# create your branch
git checkout main
git checkout -b <your-branch>

# check commit graph
git log --graph

# once finished
git push -u origin <your-branch>
```

Your goal for each exercise is to do what is asked and end up with the given commit graph on your branch.

Initial graph of main branch:

```
o Set answer
|
o Comment
|
o First version
|
```

The exercices are bases on a small python script:

```bash
python deep_thought.py
```

Here are some documentation to help you:

- https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
- https://www.atlassian.com/git/tutorials/rewriting-history

## Exercise 1: amend

Modify "Set answer" commit by changing the answer in `data.json` to its number (commit information (author, title, ...) should be kept).

```
o Set answer
|
o Comment
|
o First version
|
```

## Exercise 2: squash

Merge the two last commits together.

```
o Set answer + Comment
|
o First version
|
```

## Exercise 3: rename

Rename "Comment" commit to "Add comments".

```
o Set answer
|
o Add comments
|
o First version
|
```

## Exercise 4: reorder

Swap the two commits "Set answer" and "Comment"

```
o Comment
|
o Set answer
|
o First version
|
```

## Exercise 5: delete

Delete "Comment" commit

```
o Set answer
|
o First version
|
```

## Exercise 6: merge

Merge the branch `feature/question` to your branch and resolve the conflict (keep numbers)

```
o Merge branch 'feature/question' from ...
|
o Set answer
|
o Comment
|
o First version
|
```

## Exercise 7: rebase

Move the commit in the branch `feature/question` after your branch

```
o Add question
|
o Set answer
|
o Comment
|
o First version
|
```
