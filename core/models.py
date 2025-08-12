from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_img = models.ImageField(upload_to='users/', blank=True, null=True)
    current_boost_used = models.BooleanField(default=False)
    pass


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='creator_profile')
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='creators/', blank=True, null=True)
    twitch_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    tik_tok_url = models.URLField(blank=True)
    discord_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

class VotingPeriod(models.Model):
    title = models.CharField(max_length=5)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"The contest for {self.title} is now active until {self.end_date.strftime('%Y-%m-%d %H:%M:%S')}!"
    

class Vote(models.Model):
    STANDARD = 'standard'
    BOOSTED = 'boosted'
    VOTE_TYPE_CHOICES = [
        (STANDARD, 'Standard'),
        (BOOSTED, 'Boosted'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='votes_received')
    vote_type = models.CharField(max_length=10, choices=VOTE_TYPE_CHOICES, default=STANDARD)
    voting_period = models.ForeignKey(VotingPeriod, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'creator', 'voting_period')
    
    def __str__(self):
        return f"{self.user.username} boosted {self.creator.user.username} for {self.voting_period.title}.!"
    

class HallOfFame(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='hall_of_fame_entries')
    voting_period = models.OneToOneField(VotingPeriod, on_delete=models.CASCADE, related_name='hall_of_fame_entry')
    date_won = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.creator.user.username} - is the winner of {self.voting_period.title}"
