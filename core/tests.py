from django.test import TestCase
from faker import Faker
from .models import User, Creator, VotingPeriod, Vote, HallOfFame
from django.utils import timezone


faker = Faker()
now = timezone.now()

class CreateVotingSystem(TestCase):    
    def test_account_creation(self):
        self.users = [
            User.objects.create_user(
            username=faker.user_name(),
            email=faker.email(),
            password='testpassword123'
            )
        for _ in range(10)
        ]
        
        self.creators = [
            Creator.objects.create(
                user=user,
                bio=faker.text(),
                profile_img=None,
                twitch_url=faker.url(),
                youtube_url=faker.url(),
                x_url=faker.url(),
                instagram_url=faker.url(),
                tik_tok_url=faker.url(),
                discord_url=faker.url(),
                website_url=faker.url(),
                github_url=faker.url(),
                created_at=now
        )for user in self.users[:4]
        ]        

        self.voting_periods = [
            VotingPeriod.objects.create(
                title=faker.word()[:5],
                start_date=now,
                end_date=now + timezone.timedelta(days=6),
                is_active=True
            )
            for _ in range(3)
        ]
        
        self.vote = Vote.objects.create(
            user=self.users[0],
            creator=self.creators[0],
            vote_type=Vote.BOOSTED,
            voting_period=self.voting_periods[0]
        )
        
        #print(self.users, self.creators, self.voting_periods, self.vote)
        #print(self.creators[0].user.username, self.creators[0].tik_tok_url)
        
        self.assertEqual(len(self.users), 10)
        self.assertEqual(len(self.creators), 4)
        self.assertEqual(len(self.voting_periods), 3)
        self.assertEqual(self.vote.vote_type, Vote.BOOSTED)
        self.assertEqual(self.vote.voting_period, self.voting_periods[0])
        self.assertEqual(self.vote.creator, self.creators[0])
        self.assertEqual(self.vote.user, self.users[0])