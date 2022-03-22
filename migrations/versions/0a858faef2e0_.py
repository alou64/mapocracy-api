"""empty message

Revision ID: 0a858faef2e0
Revises: 8e15bad96cb4
Create Date: 2022-03-22 09:10:05.872948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a858faef2e0'
down_revision = '8e15bad96cb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voter_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_table('voter_list_member',
    sa.Column('voter_list_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['public.user.id'], ),
    sa.ForeignKeyConstraint(['voter_list_id'], ['public.voter_list.id'], ),
    sa.PrimaryKeyConstraint('voter_list_id', 'user_id'),
    schema='public'
    )
    op.drop_table('email_list_member')
    op.drop_table('email_list')
    op.drop_constraint('answer_poll_id_fkey', 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'poll', ['poll_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('poll_user_id_fkey', 'poll', type_='foreignkey')
    op.drop_constraint('poll_category_id_fkey', 'poll', type_='foreignkey')
    op.create_foreign_key(None, 'poll', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'poll', 'voter_list', ['restriction'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'poll', 'category', ['category_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('vote_user_id_fkey', 'vote', type_='foreignkey')
    op.drop_constraint('vote_answer_id_fkey', 'vote', type_='foreignkey')
    op.drop_constraint('vote_poll_id_fkey', 'vote', type_='foreignkey')
    op.create_foreign_key(None, 'vote', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'vote', 'poll', ['poll_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'vote', 'answer', ['answer_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.create_foreign_key('vote_poll_id_fkey', 'vote', 'poll', ['poll_id'], ['id'])
    op.create_foreign_key('vote_answer_id_fkey', 'vote', 'answer', ['answer_id'], ['id'])
    op.create_foreign_key('vote_user_id_fkey', 'vote', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.create_foreign_key('poll_category_id_fkey', 'poll', 'category', ['category_id'], ['id'])
    op.create_foreign_key('poll_user_id_fkey', 'poll', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'answer', schema='public', type_='foreignkey')
    op.create_foreign_key('answer_poll_id_fkey', 'answer', 'poll', ['poll_id'], ['id'])
    op.create_table('email_list',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('email_list_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='email_list_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='email_list_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('email_list_member',
    sa.Column('email_list_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['email_list_id'], ['email_list.id'], name='email_list_member_email_list_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='email_list_member_user_id_fkey'),
    sa.PrimaryKeyConstraint('email_list_id', 'user_id', name='email_list_member_pkey')
    )
    op.drop_table('voter_list_member', schema='public')
    op.drop_table('voter_list', schema='public')
    # ### end Alembic commands ###
