from django.db import models

__all__ = (
    'BlogUser',
)

class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
        related_name='my_friends',
        symmetrical=False,
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_friends',
        symmetrical=False,
    )

    @property
    def posts(self):
        return f'내가 작성한 글 목록: {self.post_set.all()}'

    @property
    def comments(self):
        return f'내가 작성한 댓글 목록: {self.my_comment.all()}'

    def __str__(self):
        return self.name